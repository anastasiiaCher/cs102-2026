"""sudoku solver. i still hate pylint"""

import pathlib
import random as rd
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    """creates a sudoku grid"""
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)))
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """

    mt_1: tp.List[tp.List[T]] = [[] for _ in range((len(values) + n - 1) // n)]

    for _, elem in enumerate(values):
        mt_1[_ // n].append(elem)

    return mt_1


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    list_row = grid[pos[0]]

    return list_row


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """

    list_col = []

    for _ in grid:
        list_col.append(_[pos[1]])

    return list_col


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """

    list_block = []

    start_row = [(pos[0] // 3) * 3, (pos[0] // 3) * 3 + 1, (pos[0] // 3) * 3 + 2]
    start_col = [(pos[1] // 3) * 3, (pos[1] // 3) * 3 + 1, (pos[1] // 3) * 3 + 2]

    for i in start_row:
        for j in start_col:
            list_block.append(grid[i][j])

    return list_block


def find_empty_positions(
    grid: tp.List[tp.List[str]],
) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for row, _ in enumerate(grid):
        if "." in _:
            for col, __ in enumerate(_):
                if __ == ".":
                    return row, col

    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """

    num = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    list_row = set(get_row(grid, pos))
    list_col = set(get_col(grid, pos))
    list_block = set(get_block(grid, pos))

    return num - list_block - list_row - list_col


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid"""
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    ... [['5', '3', '4', '6', '7', '8', '9', '1', '2'], 
    ... ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
    ... ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
    ... ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
    ... ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
    ... ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
    ... ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
    ... ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
    ... ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    pos_empty = find_empty_positions(grid)
    if pos_empty is None:
        return grid

    possible_values = find_possible_values(grid, pos_empty)

    for _ in possible_values:
        grid[pos_empty[0]][pos_empty[1]] = _

        solution = solve(grid)

        if solution is not None:
            return grid

        grid[pos_empty[0]][pos_empty[1]] = "."

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False
    >>> correct = [
    ...     ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ...     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ...     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ...     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ...     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ...     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ...     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ...     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ...     ['3', '4', '5', '2', '8', '6', '1', '7', '9']
    ... ]
    >>> check_solution(correct)
    True
    >>> incorrect = [
    ...     ['5', '3', '4', '6', '7', '8', '9', '1', '5'],
    ...     ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ...     ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ...     ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ...     ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ...     ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ...     ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ...     ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ...     ['3', '4', '5', '2', '8', '6', '1', '7', '9']
    ... ]
    >>> check_solution(incorrect)
    False
    """

    num = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    for i in range(9):
        if set(get_row(solution, (i, 0))) != num:
            return False
        if set(get_col(solution, (0, i))) != num:
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if set(get_block(solution, (row, col))) != num:
                return False

    return True


def generate_sudoku(n: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    grid = group(["."] * 81, 9)

    n = min(n, 81)

    seed_num = min(17, n)
    # чтобы у судоку было единственное
    # решение, изначально должно стоять
    # не менее 17 цифр. если N < 17,
    # берем min(N, 17)

    seed_cnt = 0
    while seed_cnt < seed_num:
        row = rd.randint(0, 8)
        col = rd.randint(0, 8)
        digit = str(rd.randint(1, 9))

        if grid[row][col] == "." and digit in find_possible_values(grid, pos=(row, col)):
            grid[row][col] = digit
            seed_cnt += 1

    solved_grid = solve(grid)

    if solved_grid is not None:
        dots_num = 81 - n

        while dots_num > 0:
            row = rd.randint(0, 8)
            col = rd.randint(0, 8)
            if solved_grid[row][col] != ".":
                solved_grid[row][col] = "."
                dots_num -= 1

        return solved_grid

    return generate_sudoku(n)


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid_1 = read_sudoku(fname)
        display(grid_1)
        solution_1 = solve(grid_1)
        if not solution_1:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution_1)

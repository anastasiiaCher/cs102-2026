import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
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
    return [values[value : value + n] for value in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    return [value[pos[1]] for value in grid]


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
    # По введенной позиции определяем координаты, с которых начинается искомый квадрат
    start_row = (pos[0] // 3) * 3
    start_col = (pos[1] // 3) * 3

    return [grid[row][col] for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3)]


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
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if value == ".":
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
    all_values = set("123456789")
    used_values = set(get_row(grid, pos) + get_col(grid, pos) + get_block(grid, pos))
    return all_values - used_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid
    :rtype: tp.Optional[tp.List[tp.List[str]]]
    """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    pos = find_empty_positions(grid)
    if not pos:
        return grid

    for value in find_possible_values(grid, pos):
        grid[pos[0]][pos[1]] = value
        solved_sudoku = solve(grid)
        if solved_sudoku:
            return solved_sudoku
        grid[pos[0]][pos[1]] = "."
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False
    Правильное решение:
    >>> good = [
    ...     ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ...     ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ...     ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ...     ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ...     ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ...     ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ...     ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ...     ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ...     ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ... ]
    >>> check_solution(good)
    True

    Не до конца решённый пазл (в последней клетке точка):
    >>> not_solved = [
    ...     ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ...     ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ...     ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ...     ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ...     ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ...     ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ...     ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ...     ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ...     ["3", "4", "5", "2", "8", "6", "1", "7", "."],
    ... ]
    >>> check_solution(not_solved)
    False

    Повторы в первой строке:
    >>> bad = [
    ...     ["6", "6", "1", "1", "1", "5", "8", "3", "7"],
    ...     ["3", "5", "7", "8", "2", "6", "1", "4", "9"],
    ...     ["1", "4", "8", "9", "3", "7", "5", "2", "6"],
    ...     ["6", "3", "9", "5", "1", "2", "4", "7", "8"],
    ...     ["5", "8", "1", "7", "6", "4", "3", "9", "2"],
    ...     ["4", "7", "2", "3", "9", "8", "6", "1", "5"],
    ...     ["9", "6", "4", "2", "8", "3", "7", "5", "1"],
    ...     ["8", "1", "5", "4", "7", "9", "2", "6", "3"],
    ...     ["7", "2", "3", "6", "5", "1", "9", "8", "4"],
    ... ]
    >>> check_solution(bad)
    False

    Строки правильные, столбцы состоят из одинаковых цифр:
    >>> same_rows = [["1", "2", "3", "4", "5", "6", "7", "8", "9"]] * 9
    >>> check_solution(same_rows)
    False

    В каждой строке одна и та же цифра:
    >>> same_digits = [
    ...     ["1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ...     ["2", "2", "2", "2", "2", "2", "2", "2", "2"],
    ...     ["3", "3", "3", "3", "3", "3", "3", "3", "3"],
    ...     ["4", "4", "4", "4", "4", "4", "4", "4", "4"],
    ...     ["5", "5", "5", "5", "5", "5", "5", "5", "5"],
    ...     ["6", "6", "6", "6", "6", "6", "6", "6", "6"],
    ...     ["7", "7", "7", "7", "7", "7", "7", "7", "7"],
    ...     ["8", "8", "8", "8", "8", "8", "8", "8", "8"],
    ...     ["9", "9", "9", "9", "9", "9", "9", "9", "9"],
    ... ]
    >>> check_solution(same_digits)
    False
    """

    digits = set("123456789")

    for row_num in range(9):
        if set(get_row(solution, (row_num, 0))) != digits:
            return False
    for col_num in range(9):
        if set(get_col(solution, (0, col_num))) != digits:
            return False
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            if set(get_block(solution, (r, c))) != digits:
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
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
    grid = [["."] * 9 for _ in range(9)]

    # Случайно заполняем три диагональных блока
    for start in (0, 3, 6):
        digits = list("123456789")
        random.shuffle(digits)
        for i in range(3):
            for j in range(3):
                grid[start + i][start + j] = digits[i * 3 + j]

    # Достраиваем до полного решения
    solved = solve(grid)
    if solved is None:
        raise ValueError("Не удалось построить судоку")
    grid = solved

    # Стираем лишние клетки
    N = max(0, min(N, 81))
    positions = [(row, col) for row in range(9) for col in range(9)]
    for row, col in random.sample(positions, 81 - N):
        grid[row][col] = "."

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)

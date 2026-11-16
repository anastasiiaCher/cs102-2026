"""
Решатель Судоку
"""

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
    """Создание Судоку"""
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
    return [values[i : i + n] for i in range(0, len(values), n)]


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
    return [grid[row][pos[1]] for row in range(len(grid))]


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
    row, col = pos
    block_row = row // 3
    block_col = col // 3
    row_start = block_row * 3
    col_start = block_col * 3
    return [grid[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == ".":
                return (i, j)
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
    universum = set("123456789")
    row_values = set(get_row(grid, pos))
    col_values = set(get_col(grid, pos))
    block_values = set(get_block(grid, pos))
    used = row_values.union(col_values, block_values)
    used.remove(".")
    return universum.difference(used)


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
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty = find_empty_positions(grid)
    # если нет свободных клеток, пазл решен
    if not empty:
        return grid

    # получаем первую свободную клетку, ищем возможные значения
    row, col = empty
    possible_values = find_possible_values(grid, empty)

    for value in possible_values:
        grid[row][col] = value  # поставили значение на свободную позицию
        solution = solve(grid)  # продолжаем решение судоку
        if solution:
            return solution
        grid[row][col] = "."  # откат действия назад, если не получилось решить
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    if not solution:
        return False

    universum = set("123456789")
    # проверяем строки и столбцы
    for i in range(len(solution)):
        row_values = set(get_row(solution, (i, 0)))
        if set(row_values) != universum:
            return False
        col_values = set(get_col(solution, (0, i)))
        if set(col_values) != universum:
            return False

    # проверяем все квадраты 3x3
    for block_row in range(3):
        for block_col in range(3):
            pos = (block_row * 3, block_col * 3)
            block_values = set(get_block(solution, pos))
            if block_values != universum:
                return False

    return True


def generate_sudoku(n_elem: int) -> tp.List[tp.List[str]]:
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
    # берем готовое решение, часть цифр случайно убираем
    base = [
        "123456789",
        "456789123",
        "789123456",
        "234567891",
        "567891234",
        "891234567",
        "345678912",
        "678912345",
        "912345678",
    ]

    # Случайно перемешиваем цифры
    digits = list("123456789")
    random.shuffle(digits)
    # словарь для замены исходных цифр на цифры из перемешанного списка
    mapping = dict(zip("123456789", digits))

    # Случайно перемешиваем группы по 3 строки
    bands = [0, 3, 6]  # индексы первых строк групп по 3 строки (полос)
    random.shuffle(bands)  # перемешиваем порядок этих первых строк => порядок полос
    rows = []
    for band in bands:  # проходим по первым строкам перемешанных полос
        inner = [band, band + 1, band + 2]  # список из трёх строк этой полосы
        random.shuffle(inner)  # перемешиваем порядок строк внутри полосы
        rows.extend(inner)

    # Случайно перемешиваем группы по 3 столбца (аналогично строкам)
    stacks = [0, 3, 6]
    random.shuffle(stacks)
    cols = []
    for stack in stacks:
        inner = [stack, stack + 1, stack + 2]
        random.shuffle(inner)
        cols.extend(inner)

    # Собираем полностью решённую доску
    grid = [[mapping[base[r][c]] for c in cols] for r in rows]

    assert check_solution(grid) is True
    # Случайно стираем 81 - N клеток
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    for r, c in cells[: 81 - n_elem]:
        grid[r][c] = "."

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
            if check_solution(solution):
                print("Solution is correct")
            else:
                print("Ooops")

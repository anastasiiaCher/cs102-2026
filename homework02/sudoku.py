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
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "")
                for col in range(9)
            )
        )
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
    pass


def get_row(
    grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]
) -> tp.List[str]:  # pos - кортеж из двух чисел (строка, столбец) -> это в сл команде
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos  # придаем значения числам кортежа
    return grid[row]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos
    return [
        grid[r][col] for r in range(len(grid))
    ]  # r тут - переменная для перебора строк
    pass


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
    start_row = (
        row // 3
    ) * 3  # вычисляем, вначале нужный квадрат 3×3, а потом с какой строки начинается нужный квадрат
    start_col = (col // 3) * 3
    block = []
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            block.append(grid[r][c])
    return block
    pass


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
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == ".":
                return (r, c)
    return None
    pass


def find_possible_values(
    grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]
) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    row_vals = set(get_row(grid, pos))
    col_vals = set(get_col(grid, pos))
    block_vals = set(get_block(grid, pos))

    used_vals = row_vals.union(col_vals).union(block_vals)
    all_vals = set("123456789")

    return all_vals - used_vals
    pass


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
    # ищем первую пустую клетку
    pos = find_empty_positions(grid)

    # если пустых клеток нет, пазл решен
    if pos is None:
        return grid

    # готовимся к перебору
    row, col = pos
    possible_values = find_possible_values(grid, pos)

    # перебираем все цифры, которые можно поставить
    for val in possible_values:
        grid[row][col] = val  # пробуем поставить цифру

        # рекурсия: просим функцию решить остаток пазла
        if solve(grid) is not None:
            return grid  # Если получилось, возвращаем решение

        grid[row][col] = "."  # Откат: стираем цифру, если зашли в тупик

    # Если ни одна цифра не подошла, возвращаем None (тупик)
    return None
    pass


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    # TODO: Add doctests with bad puzzles
    """
        >>> bad_solution = [
    ...     ['6', '6', '1', '1', '1', '5', '8', '3', '7'],
    ...     ['3', '5', '7', '8', '2', '6', '1', '4', '9'],
    ...     ['1', '4', '8', '9', '3', '7', '5', '2', '6'],
    ...     ['6', '3', '9', '5', '1', '2', '4', '7', '8'],
    ...     ['5', '8', '1', '7', '6', '4', '3', '9', '2'],
    ...     ['4', '7', '2', '3', '9', '8', '6', '1', '5'],
    ...     ['9', '6', '4', '2', '8', '3', '7', '5', '1'],
    ...     ['8', '1', '5', '4', '7', '9', '2', '6', '3'],
    ...     ['7', '2', '3', '6', '5', '1', '9', '8', '4']]
    >>> check_solution(bad_solution)
    False
    """
    # Проверяем все 9 строк и 9 столбцов
    for i in range(9):
        row = get_row(solution, (i, 0))
        if set(row) != set("123456789"):
            return False
        col = get_col(solution, (0, i))
        if set(col) != set("123456789"):
            return False
    # Проверяем все 9 квадратов 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = get_block(solution, (i, j))
            if set(block) != set("123456789"):
                return False
    return True
    pass


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
    # cоздаём полностью решённое Судоку
    grid = solve([["."] * 9 for _ in range(9)])

    # вычисляем, сколько клеток нужно очистить
    cells_to_remove = max(0, 81 - N)

    # создаём список всех позиций и перемешиваем
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    # заменяем случайные клетки на точки
    for r, c in positions[:cells_to_remove]:
        grid[r][c] = "."

    return grid
    pass


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)

import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
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
    if n <= 0:
        raise ValueError("Размер группы должен быть положительным")

    return [values[i:i + n] for i in range(0, len(values), n)]

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row_index, _ = pos
    return grid[row_index].copy()


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    _, col_index = pos
    return [row[col_index] for row in grid]


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
    row_index, col_index = pos

    first_row = (row_index // 3) * 3
    first_col = (col_index // 3) * 3

    return [
        grid[row][col]
        for row in range(first_row, first_row + 3)
        for col in range(first_col, first_col + 3)
    ]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value == ".":
                return row_index, col_index

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
 row_index, col_index = pos

    if grid[row_index][col_index] != ".":
        return set()

    used_values = (
        set(get_row(grid, pos))
        | set(get_col(grid, pos))
        | set(get_block(grid, pos))
    )

    return set("123456789") - used_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
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
    working_grid = [row.copy() for row in grid]

    def search() -> bool:
        position = find_empty_positions(working_grid)

        # Пустых клеток больше нет — поле заполнено.
        if position is None:
            return True

        row_index, col_index = position

        for value in sorted(find_possible_values(working_grid, position)):
            working_grid[row_index][col_index] = value

            if search():
                return True

            # Эта цифра не подошла — очищаем клетку и пробуем следующую.
            working_grid[row_index][col_index] = "."

        return False

    if search():
        return working_grid

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
        if len(solution) != 9 or any(len(row) != 9 for row in solution):
        return False

    required_values = set("123456789")

    # Проверяем строки.
    for row in solution:
        if set(row) != required_values:
            return False

    # Проверяем столбцы.
    for col_index in range(9):
        column = {
            solution[row_index][col_index]
            for row_index in range(9)
        }
        if column != required_values:
            return False

    # Проверяем квадраты 3×3.
    for first_row in range(0, 9, 3):
        for first_col in range(0, 9, 3):
            block = {
                solution[row][col]
                for row in range(first_row, first_row + 3)
                for col in range(first_col, first_col + 3)
            }
            if block != required_values:
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
        base_grid = [
        [(row * 3 + row // 3 + col) % 9 for col in range(9)]
        for row in range(9)
    ]

    # Перемешиваем группы строк и строки внутри групп.
    row_groups = random.sample(range(3), 3)
    rows = [
        group_index * 3 + row
        for group_index in row_groups
        for row in random.sample(range(3), 3)
    ]

    # Перемешиваем группы столбцов и столбцы внутри групп.
    col_groups = random.sample(range(3), 3)
    cols = [
        group_index * 3 + col
        for group_index in col_groups
        for col in random.sample(range(3), 3)
    ]

    # Перемешиваем цифры.
    digits = random.sample("123456789", 9)

    grid = [
        [digits[base_grid[row][col]] for col in cols]
        for row in rows
    ]

    # Ограничиваем количество заполненных клеток диапазоном 0–81.
    filled_cells = max(0, min(N, 81))
    empty_cells_count = 81 - filled_cells

    all_positions = [
        (row, col)
        for row in range(9)
        for col in range(9)
    ]

    # Заменяем случайные клетки точками.
    for row, col in random.sample(all_positions, empty_cells_count):
        grid[row][col] = "."

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
       if solution is None:
            print(f"Puzzle {fname} can't be solved")
        elif check_solution(solution):
            display(solution)
            print("Solution is correct")
        else:
            print("Ooops")

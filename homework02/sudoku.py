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
        print(" ".join(grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)))
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
    """Возвращает все значения для номера строки, указанной в pos"""
    row, _ = pos
    return grid[row]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos"""
    _, col = pos
    return [grid[row][col] for row in range(len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    row, col = pos
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    block = []
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            block.append(grid[r][c])
    return block


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                return (i, j)
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значений для указанной позиции"""
    all_values = set("123456789")
    used_in_row = set(get_row(grid, pos))
    used_in_col = set(get_col(grid, pos))
    used_in_block = set(get_block(grid, pos))

    # Убираем точку из использованных, если она там есть
    used_values = (used_in_row | used_in_col | used_in_block) - {"."}

    return all_values - used_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid"""
    empty_pos = find_empty_positions(grid)
    if not empty_pos:
        return grid

    row, col = empty_pos
    possible_values = find_possible_values(grid, (row, col))

    for value in possible_values:
        grid[row][col] = value
        solution = solve(grid)
        if solution:
            return solution
        grid[row][col] = "."

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение верно, то вернуть True, False"""
    for i in range(9):
        row = set(get_row(solution, (i, 0)))
        if len(row) != 9 or "." in row:
            return False

    for j in range(9):
        col = set(get_col(solution, (0, j)))
        if len(col) != 9 or "." in col:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = set(get_block(solution, (i, j)))
            if len(block) != 9 or "." in block:
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""
    base_grid = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]

    # Копируем базовое решение
    full_grid = [row[:] for row in base_grid]

    # Удаляем случайные элементы, пока не останется N
    cells_to_remove = 81 - N
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    for i in range(cells_to_remove):
        r, c = positions[i]
        full_grid[r][c] = "."

    return full_grid


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
                print("Nope")

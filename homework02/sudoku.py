import pathlib
import random
import typing as tp

T = tp.TypeVar("T")


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[i : i + n] for i in range(0, len(values), n)]


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку в консоль"""
    for row in range(9):
        line = ""
        for col in range(9):
            line += grid[row][col] + " "
            if col % 3 == 2 and col != 8:
                line += "| "
        print(line)
        if row % 3 == 2 and row != 8:
            print("------+-------+------")


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
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    block = []
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            block.append(grid[r][c])
    return block


def find_empty_positions(
    grid: tp.List[tp.List[str]],
) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                return (row, col)
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество всех возможных значения для указанной позиции"""
    row_vals = set(get_row(grid, pos))
    col_vals = set(get_col(grid, pos))
    block_vals = set(get_block(grid, pos))
    used_values = row_vals.union(col_vals).union(block_vals)

    all_values = set("123456789")

    return all_values - used_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Поиск решения для указанного пазла."""
    pos = find_empty_positions(grid)
    if not pos:
        return grid

    possible_values = find_possible_values(grid, pos)

    for val in possible_values:
        row, col = pos
        grid[row][col] = val

        if solve(grid):
            return grid

        grid[row][col] = "."

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    if not solution:
        return False

    expected = set("123456789")

    for i in range(9):
        if set(solution[i]) != expected:
            return False
        if set(get_col(solution, (0, i))) != expected:
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if set(get_block(solution, (row, col))) != expected:
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""
    grid = [["." for _ in range(9)] for _ in range(9)]

    for i in range(0, 9, 3):
        nums = list("123456789")
        random.shuffle(nums)
        for r in range(3):
            for c in range(3):
                grid[i + r][i + c] = nums.pop()

    solved_grid = solve(grid)

    if not solved_grid:
        return generate_sudoku(N)

    cells_to_clear = 81 - min(N, 81)
    all_cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(all_cells)

    for _ in range(cells_to_clear):
        r, c = all_cells.pop()
        solved_grid[r][c] = "."

    return solved_grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)

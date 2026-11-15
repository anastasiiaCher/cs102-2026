import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Чтение Судоку из указанного файла"""
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
    """Сгруппировать значения values в список, состоящий из списков по n элементов"""
    return [values[i : i + n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos"""
    row, col = pos
    return grid[row]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанной в pos"""
    row, col = pos
    return [line[col] for line in grid]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    row, col = pos

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    return [grid[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                return row, col

    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции"""
    all_values = set("123456789")

    used_values = set(get_row(grid, pos))
    used_values.update(get_col(grid, pos))
    used_values.update(get_block(grid, pos))

    return all_values - used_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid"""
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла """
    pos = find_empty_positions(grid)

    if pos is None:
        return grid

    row, col = pos

    possible_values = sorted(find_possible_values(grid, pos))

    for value in possible_values:
        grid[row][col] = value

        result = solve(grid)

        if result is not None:
            return result

        grid[row][col] = "."

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    if len(solution) != 9:
        return False

    if any(len(row) != 9 for row in solution):
        return False

    expected_values = set("123456789")

    for row in solution:
        if set(row) != expected_values:
            return False

    for col in range(9):
        if set(get_col(solution, (0, col))) != expected_values:
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if set(get_block(solution, (row, col))) != expected_values:
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов"""
    N = max(0, min(N, 81))

    grid = [[str((row * 3 + row // 3 + col) % 9 + 1) for col in range(9)] for row in range(9)]

    digits = list("123456789")
    shuffled_digits = digits.copy()
    random.shuffle(shuffled_digits)

    replacements = dict(zip(digits, shuffled_digits))

    for row in range(9):
        for col in range(9):
            grid[row][col] = replacements[grid[row][col]]

    empty_positions = random.sample([(row, col) for row in range(9) for col in range(9)], 81 - N)

    for row, col in empty_positions:
        grid[row][col] = "."

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)

        solution = solve(grid)

        if solution is None:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)

            if check_solution(solution):
                print("Solution is correct")
            else:
                print("Ooops")

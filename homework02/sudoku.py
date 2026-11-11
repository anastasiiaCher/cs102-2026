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


# Наша реализация. Разбиваем список на группы по n элементов.
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
    # range даёт начала групп, срез берёт до n элементов.
    return [values[start : start + n] for start in range(0, len(values), n)]


# Наша реализация. Возвращаем всю строку по первой координате клетки.
def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row_index = pos[0]
    return grid[row_index]


# Наша реализация. Собираем столбец, беря по одной клетке из каждой строки.
def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    col_index = pos[1]
    column = []

    for row in grid:
        column.append(row[col_index])

    return column


# Наша реализация. Собираем девять клеток блока 3×3 в один список.
def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> puzzle_grid = read_sudoku('puzzle1.txt')
    >>> get_block(puzzle_grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(puzzle_grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(puzzle_grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    # Деление на 3 даёт номер тройки, умножение — её начальный индекс.
    start_row = (pos[0] // 3) * 3
    start_col = (pos[1] // 3) * 3
    block = []

    for row in grid[start_row : start_row + 3]:
        part = row[start_col : start_col + 3]
        # extend добавляет клетки по одной, сохраняя плоский список.
        block.extend(part)

    return block


# Наша реализация. Ищем первую точку сверху вниз и слева направо.
def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    # enumerate даёт индекс и значение, чтобы вернуть адрес точки.
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == ".":
                return row_index, col_index

    return None


# Наша реализация. Исключаем цифры, уже занятые в строке, столбце или блоке.
def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> puzzle_grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(puzzle_grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(puzzle_grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    all_digits = set("123456789")
    row = get_row(grid, pos)
    column = get_col(grid, pos)
    block = get_block(grid, pos)
    # Соединяем три списка и убираем повторы перед вычитанием.
    used_digits = set(row + column + block)
    return all_digits - used_digits


# Наша реализация. Решаем судоку рекурсивным перебором с возвратом.
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
    pos = find_empty_positions(grid)
    # Условие остановки рекурсии: все клетки заполнены.
    if pos is None:
        return grid

    row_index = pos[0]
    col_index = pos[1]

    for digit in sorted(find_possible_values(grid, pos)):
        grid[row_index][col_index] = digit
        # Рекурсия: с пробной цифрой в этой клетке решаем остаток поля.
        solution = solve(grid)
        if solution is not None:
            return solution

        # Откат: стираем пробную цифру перед следующим вариантом.
        grid[row_index][col_index] = "."

    return None


# Наша реализация. Проверяем размеры поля и цифры во всех строках, столбцах и блоках.
def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    all_digits = set("123456789")
    if len(solution) != 9:
        return False

    for row in solution:
        if len(row) != 9 or set(row) != all_digits:
            return False

    for col_index in range(9):
        column = get_col(solution, (0, col_index))
        if set(column) != all_digits:
            return False

    # Углы блоков находятся на индексах 0, 3 и 6 по обеим координатам.
    for row_index in range(0, 9, 3):
        for col_index in range(0, 9, 3):
            block = get_block(solution, (row_index, col_index))
            if set(block) != all_digits:
                return False

    return True


# Наша реализация. Создаём решаемый пазл с заданным числом подсказок.
# noinspection PyPep8Naming
def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> puzzle_grid = generate_sudoku(40)
    >>> sum(1 for row in puzzle_grid for e in row if e == '.')
    41
    >>> solved_grid = solve(puzzle_grid)
    >>> solved_grid is not None and check_solution(solved_grid)
    True
    >>> puzzle_grid = generate_sudoku(1000)
    >>> sum(1 for row in puzzle_grid for e in row if e == '.')
    0
    >>> solved_grid = solve(puzzle_grid)
    >>> solved_grid is not None and check_solution(solved_grid)
    True
    >>> puzzle_grid = generate_sudoku(0)
    >>> sum(1 for row in puzzle_grid for e in row if e == '.')
    81
    >>> solved_grid = solve(puzzle_grid)
    >>> solved_grid is not None and check_solution(solved_grid)
    True
    """
    grid = [["."] * 9 for _ in range(9)]
    # Случайно заполняем первую строку, затем решаем всё поле.
    grid[0] = random.sample("123456789", 9)
    solution = solve(grid)
    assert solution is not None

    # Ограничиваем число подсказок и выбираем клетки без повторов.
    filled_cells = max(0, min(N, 81))
    for position in random.sample(range(81), 81 - filled_cells):
        # Частное даёт номер строки, остаток — номер столбца.
        row_index = position // 9
        col_index = position % 9
        solution[row_index][col_index] = "."

    return solution


if __name__ == "__main__":
    for puzzle_file in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        initial_board = read_sudoku(puzzle_file)
        display(initial_board)
        solved_board = solve(initial_board)
        if solved_board is None:
            print(f"Puzzle {puzzle_file} can't be solved")
        else:
            display(solved_board)
            # Наша проверка: выводим результат проверки готового поля.
            if check_solution(solved_board):
                print("Solution is correct")
            else:
                print("Ooops")

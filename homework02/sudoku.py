"""
Судоку. Лабораторная по програмированию
"""

import pathlib
import random
import typing as tp

T = tp.TypeVar("T")

all_digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
# [1:] убирает 0


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open(encoding="utf-8") as f:
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
    # через списковое включение
    # range генерирует стартовые индексы для каждого кусочка (шаг n)
    # values делает срез списка, вырезая ровно n элементов, начиная с индекса i.
    # скобки дают матрицу из полученного
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
    # распаковка последовательностей
    row, _ = pos
    # _ вместо col для чистоты кода
    # а дальше в ретюрн просто берём индекс
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
    # также распаковка
    _, col = pos
    # уже проходимся циклом по строчкам, беря тот элемент,что нужен  через индекс
    return [r[col] for r in grid]


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
    # распаковка снова
    row, col = pos
    # получаем номер стоки и столбца
    # уже внутри этого кважратика 3 на 3
    # (он может быть 4 вообще, но первым в этой квадратике)
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    return [
        # обращаемся к нужному месту для числа
        grid[r][c]
        # берём оставшиеся места в квадрате 3 на 3 от этой извлеченого места
        for r in range(start_row, start_row + 3)
        for c in range(start_col, start_col + 3)
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
    # проверяем последовательность сначала по строцкам, потом столбцам
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                return (row, col)
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
    # делаем множество (set) из свободных мест на стрчоках и стобцах, а также невозможные места
    row_vals = set(get_row(grid, pos))
    col_vals = set(get_col(grid, pos))
    block_vals = set(get_block(grid, pos))

    # Из всех возможных цифр вычитаем те, что уже заняты в строке, столбце или квадрате
    # | -- объединение множеств
    # получаем те цифры, что могут стоять на том месте
    return all_digits - (row_vals | col_vals | block_vals)


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
    # берём свободные
    pos = find_empty_positions(grid)
    # Базовый случай: если свободных позиций нет, судоку решен
    if not pos:
        return grid

    row, col = pos
    possible_values = find_possible_values(grid, pos)

    for value in possible_values:
        grid[row][col] = value  # Поместить значение
        # Рекурсивно продолжаем решать оставшуюся часть
        solution = solve(grid)
        if solution:
            return solution
        # Откатываем действие назад (возращаем точку), если зашли в тупик
        grid[row][col] = "."
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    # Проверяем строки и столбцы
    for i in range(9):
        row = [solution[i][j] for j in range(9)]
        col = [solution[j][i] for j in range(9)]
        if set(row) != all_digits or set(col) != all_digits:
            return False

    # Проверяем квадраты 3 на 3
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            block = [solution[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]
            if set(block) != all_digits:
                return False

    return True


def generate_sudoku(n_elems: int) -> tp.List[tp.List[str]]:
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
    # поменял N на n_elems, чтобы тесты на стиль прошли
    # Берем готовое решение в качестве основы
    grid = solve(read_sudoku("puzzle1.txt"))
    assert grid is not None  # для mypy

    # Собираем координаты всех 81 клеток(9*9) и перемешиваем их
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    # Ограничиваем N в пределах от 0 до 81
    total_elems: int = max(0, min(int(n_elems), 81))

    # Количество клеток, которые нужно превратить в точки '.'
    dots_count: int = 81 - total_elems
    for i in range(dots_count):
        r, c = cells[i]
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

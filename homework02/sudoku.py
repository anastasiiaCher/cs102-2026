import pathlib
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


# создаем игровое поле grid
def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."] # списковое включение - перебор всех элементов и добавление в новый список, подходящих под условие
    grid = group(digits, 9) # деление списка из 81 символа и деление на группы по 9 элементов (каждая строка содержит по 9 клеток)
    return grid


# берется игровое поле grid и выводится в удобном виде
def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2  # задается ширина отображения каждой клетки
    line = "+".join(["-" * (width * 3)] * 3) # создание горизонтальной черты
    for row in range(9):
        print( # выведение целой строки судоку
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9) # перебор каждой клетки, выравнивание по центру, добавление вертикальной черты
            )
        )
        if str(row) in "25":
            print(line) # если строка 2 или 5, выводится горизонтальная линия
    print() # пустая строка, чтобы новый вывод начинался с новой строки


# разбиение одного большого списка элементов на несколько маленьких списков по n элементов в каждом
def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    result = []
    for i in range (0, len(values), n): # запуск цикла, перебирающего индексы исходного списка, начиная с 0 и увеличивая их каждый раз на n
        group = values [i:i + n] # берется часть элементов из values (с индексами от i до i+n), и эти элементы объединяются в отдельный список определенного размера n
        result.append(group) # добавление нового элемента в конец списка
    return result

# нахождение и возвращение всей строки игрового поля Судоку, получение любой строки по ее индексу
def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row = pos[0] # получение индекса строки из координат и сохранение его в переменную row
    return grid[row] # возвращение из игрового поля grid всю строку с индексом row


# нахождение и возвращение всего столбца игрового поля Судоку, получение любого столбца по его индексу
def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    col = pos[1] # получение индекса столбца из координат и сохранение его в переменную col
    column = []
    for row in grid: # запусr цикл, перебирающего по очереди все строки игрового поля
        column.append(row[col]) # берется элемент из текущей строки с индексом col и добавляет его в список column
    return column


# получение всех 9 значений из маленького квадрата 3 на 3
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
    row = pos[0]
    col = pos[1]
    start_row = (row // 3) * 3 # получение номера группы и индекса первой строки
    start_col = (col // 3) * 3 # получение номера группы и индекса первого столбца
    block = []
    for r in range(start_row, start_row + 3): # запуск цикла, перебирающего все 3 строки одного квадрата
        for c in range(start_col, start_col + 3): # запуск цикла, перебирающего все 3 столбца одного квадрата
            block.append(grid[r][c]) # находится нужная клетка по строке r и столбцу c и найденное значение добавляется в конец списка
    return block


# поиск пустой клетки
def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for r in range(len(grid)): # перебор всех строк (программа сама определяет размер)
        for c in range(len(grid[r])): # перебор всех клеток в текущей строке
            if grid[r][c] == '.':
                return (r, c) # возвращение координат найденной пустой клетки
    return None # пустые клетки отсутствуют


# поиск возможных значений для пустой клетки
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
    row = get_row(grid, pos) # получение всех значений строки, в которой находится выбранная клетка
    col = get_col(grid, pos) # получение всех значений столбца, в котором находится выбранная клетка
    block = get_block(grid, pos) # получение всех значений квадрата, в котором находится выбранная клетка
    possible = set("123456789") # множество цифр от 1 до 9
    possible.difference_update(row) # удаление из possible уже имеющихся цифр в строке
    possible.difference_update(col) # удаление из possible уже имеющихся цифр в столбце
    possible.difference_update(block) # удаление из possible уже имеющихся цифр в квадрате
    return possible


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
    pass


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
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
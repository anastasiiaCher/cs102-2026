import pathlib
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
    result = [] # то, куда мы запишем результат
    row = [] # временная строка, которую потом добавляем в результат
    for x in values: # рассматриваем каждый элемент в значениях
        row.append(x) # кладём элемент в конец текущей строки
        if len(row) == n: # проверяем набралась ли строка
            result.append(row) # добавляем её в результат
            row = [] # переходим на новую строку
    return result # возвращаем результат


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos # передаем в pos номер строки
    return grid[row] # возвращаем все значения из строки


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos # передаем в pos номер столбца
    result = [] # создаем пустой список для собирания ответа
    for r in grid: # r - очередная строка
        result.append(r[col]) 
        # добавляем элементы в результат,
        # проходимся по строкам, забирая нужного столбца
    return result # возвращаем результат


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
    row, col = pos # узнаем позиции
    # находим самый верхний и левый угол нашего квадрата
    top = row // 3 * 3 # находим верхнюю границу
    left = col // 3 * 3 # находим самую левую границу
    result = [] # создаем пустой список для результата
    for r in range(top, top + 3): 
        # рассматриваем самую верхнюю строку и идем до конца нащего квадрата
        for c in range(left, left + 3): 
            # проходимся по каждому номеру элемента строки слева направо до конца квадрата
            result.append(grid[r][c]) #добавляем элементы в результат
    return result # возвращаем результат


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for r in range(len(grid)): # проходимся по нашему судоку по строкам
        for c in range(len(grid[r])): # рассматриваем столбцы
            if grid[r][c] == '.': 
                # если элемент на позиции r и c равен точке
                return (r, c) #то мы возвращаем его индексы
    return None # если позиция не пустая


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
    used = get_row(grid, pos) + get_col(grid, pos) + get_block(grid, pos) 
    # запоминаем все использованные символы
    values = [] # создаем пустой список, куда сложим неиспользованные цифры
    for digit in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        # какие символы вообще могут быть использованы
        if digit not in used: # если цифра не занята
            values.append(digit) # то добавляем ее в список доступных значений
    return set(values) # возвращаем множество


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
    pos = find_empty_positions(grid) # на доступные позиции мы передаем индексы точек
    if pos is None: # если пустых клеток нет, то значит пазл решён
        return grid # просто возвращаем пазл
    row, col = pos # если нет, то передаем позиции
    for value in find_possible_values(grid, pos): # перебираем доступные значения 
        grid[row][col] = value # поставили цифру
        solution = solve(grid) # решаем дальше рекурсией
        if solution is not None: # если решение есть
            return solution # успех, отдаём наверх
        grid[row][col] = '.' # откат, если не подошло, стираем
    return None # тупик


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False

    Плохой пазл: поле ещё не решено
    >>> check_solution(read_sudoku('puzzle1.txt'))
    False

    Плохой пазл: девять одинаковых строк - в столбцах повторы
    >>> row = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    >>> check_solution([row] * 9)
    False
    """

    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    # проверка всех 9 строк
    for r in range(9): # проходимся по строкам
        if set(get_row(solution, (r, 0))) != digits: # если при взятии строки из решения
            # множество чисел не совпадает, то значит решение  неверно
            return False # возвращает false

    # проверка всех 9 столбцов
    for c in range(9): # проходимся по столбцам 
        if set(get_col(solution, (0, c))) != digits: # если при взятии столбца из решения
             # множество чисел не совпадает, то значит решение  неверно
            return False # возвращает false

    # проверяем все 9 квадратов
    for r in (0, 3, 6): # начинаем с самого левого элемента
        for c in (0, 3, 6): # и самого верхнего, 
            # то есть с левого верхнего уголка квадрата
            if set(get_block(solution, (r, c))) != digits: # смотрим если символы квадрата 
            # не совпадают с символами из множества  
                return False # возвращает false

    return True # в иных случаях все верно и возвращаем true


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
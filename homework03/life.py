import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = []
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        row, col = cell
        neighbours = []
        for row_change in (-1, 0, 1):
            for col_change in (-1, 0, 1):
                if row_change == 0 and col_change == 0:
                    continue
                neighbour_row = row + row_change
                neighbour_col = col + col_change
                if 0 <= neighbour_row < self.rows and 0 <= neighbour_col < self.cols:
                    neighbours.append(
                        self.curr_generation[neighbour_row][neighbour_col]
                    )
        return neighbours

    def get_next_generation(self) -> Grid:
        next_generation = self.create_grid()
        for row in range(self.rows):
            for col in range(self.cols):
                neighbours = sum(self.get_neighbours((row, col)))
                if self.curr_generation[row][col] == 1:
                    next_generation[row][col] = int(neighbours == 2 or neighbours == 3)
                else:
                    next_generation[row][col] = int(neighbours == 3)
        return next_generation

    def step(self) -> None:
        """Выполнить один шаг игры."""
        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """Проверить, достигнуто ли максимальное число поколений."""
        return (
            self.max_generations is not None
            and self.generations >= self.max_generations
        )

    @property
    def is_changing(self) -> bool:
        """Проверить, изменилось ли поле на последнем шаге."""
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """Прочитать состояние клеток из указанного файла."""
        filename = pathlib.Path(filename)
        lines = [
            line.strip() for line in filename.read_text().splitlines() if line.strip()
        ]
        if not lines or any(set(line) - {"0", "1"} for line in lines):
            raise ValueError("Файл должен содержать только 0 и 1")
        if any(len(line) != len(lines[0]) for line in lines):
            raise ValueError("Все строки должны быть одинаковой длины")
        game = GameOfLife((len(lines), len(lines[0])), randomize=False)
        game.curr_generation = [[int(value) for value in line] for line in lines]
        return game

    def save(self, filename: pathlib.Path) -> None:
        """Сохранить текущее поле в файл."""
        filename = pathlib.Path(filename)
        lines = ["".join(str(cell) for cell in row) for row in self.curr_generation]
        filename.write_text("\n".join(lines) + "\n")

import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)
        # Вычисляем число клеток по горизонтали и вертикали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        # Скорость протекания игры
        self.speed = speed
        self.grid = self.create_grid(randomize=True)

    def draw_lines(self) -> None:
        """Отрисовать сетку."""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру."""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()
            self.grid = self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """Создать список клеток размером cell_height на cell_width."""
        grid = []
        for _ in range(self.cell_height):
            row = []
            for _ in range(self.cell_width):
                row.append(random.randint(0, 1) if randomize else 0)
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        """Закрасить живые и мертвые клетки разными цветами."""
        for row in range(self.cell_height):
            for col in range(self.cell_width):
                color = pygame.Color("green") if self.grid[row][col] else pygame.Color("white")
                rect = (
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, color, rect)

    def get_neighbours(self, cell: Cell) -> Cells:
        """Вернуть значения соседних клеток по горизонтали, вертикали и диагоналям."""
        row, col = cell
        neighbours = []
        for row_change in (-1, 0, 1):
            for col_change in (-1, 0, 1):
                if row_change == 0 and col_change == 0:
                    continue
                neighbour_row = row + row_change
                neighbour_col = col + col_change
                if 0 <= neighbour_row < self.cell_height and 0 <= neighbour_col < self.cell_width:
                    neighbours.append(self.grid[neighbour_row][neighbour_col])
        return neighbours

    def get_next_generation(self) -> Grid:
        """Получить новое поколение клеток."""
        next_generation = self.create_grid()
        for row in range(self.cell_height):
            for col in range(self.cell_width):
                neighbours = sum(self.get_neighbours((row, col)))
                if self.grid[row][col] == 1:
                    next_generation[row][col] = int(neighbours == 2 or neighbours == 3)
                else:
                    next_generation[row][col] = int(neighbours == 3)
        return next_generation


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    game.run()

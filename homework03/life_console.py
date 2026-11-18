import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border()

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for row in range(self.life.rows):
            for col in range(self.life.cols):
                if self.life.curr_generation[row][col]:
                    screen.addstr(row + 1, col + 1, "O")
                else:
                    screen.addstr(row + 1, col + 1, " ")

    def run(self) -> None:
        screen = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        screen.nodelay(True)
        try:
            while self.life.is_changing and not self.life.is_max_generations_exceeded:
                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()
                if screen.getch() == ord("q"):
                    break
                self.life.step()
                time.sleep(0.2)
        finally:
            curses.endwin()


if __name__ == "__main__":
    Console(GameOfLife((24, 80))).run()

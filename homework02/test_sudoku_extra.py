"""Проверки границ и отката, которых нет в исходных тестах."""

import pathlib
import random
import unittest

import sudoku


class SudokuExtraTestCase(unittest.TestCase):
    def test_unsolvable_restores_grid(self):
        grid = sudoku.read_sudoku(pathlib.Path(__file__).with_name("puzzle1.txt"))
        grid[0][2] = "1"  # Локально допустимо, но противоречит единственному решению.
        original = [row[:] for row in grid]
        self.assertIsNone(sudoku.solve(grid))
        self.assertEqual(grid, original)

    def test_generated_clues_and_independent_rows(self):
        state = random.getstate()
        try:
            random.seed(42)
            for count in (-1, 0, 1, 40, 80, 81, 1000):
                grid = sudoku.generate_sudoku(count)
                original = [row[:] for row in grid]
                self.assertEqual(len({id(row) for row in grid}), 9)
                self.assertEqual(sum(v != "." for row in grid for v in row), max(0, min(count, 81)))
                result = sudoku.solve(grid)
                self.assertIsNotNone(result)
                self.assertTrue(sudoku.check_solution(result))
                for row in range(9):
                    for col in range(9):
                        if original[row][col] != ".":
                            self.assertEqual(grid[row][col], original[row][col])
        finally:
            random.setstate(state)

    def test_check_blocks_even_when_rows_and_columns_are_valid(self):
        latin_square = [[str((row + col) % 9 + 1) for col in range(9)] for row in range(9)]
        self.assertFalse(sudoku.check_solution(latin_square))

    def test_finished_grid_and_no_empty_cell(self):
        grid = sudoku.generate_sudoku(81)
        self.assertIsNone(sudoku.find_empty_positions(grid))
        self.assertIs(sudoku.solve(grid), grid)

    def test_group_remainder_and_invalid_size(self):
        self.assertEqual(sudoku.group([1, 2, 3], 2), [[1, 2], [3]])
        with self.assertRaises(ValueError):
            sudoku.group([1], 0)

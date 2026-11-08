import unittest

import sudoku


class SudokuEdgeTestCase(unittest.TestCase):
    def test_unsolvable_puzzle_restores_empty_cells(self):
        # Для (0, 7) есть кандидат 8, но после его подстановки (0, 8) не заполнить.
        grid = sudoku.create_grid("1234567.." + "........9" + "." * 63)
        original = [row[:] for row in grid]
        self.assertIsNone(sudoku.solve(grid))
        self.assertEqual(original, grid)

    def test_check_solution_rejects_invalid_blocks(self):
        # В каждой строке и колонке цифры уникальны, но блоки 3 на 3 неверны.
        grid = [[str((row + col) % 9 + 1) for col in range(9)] for row in range(9)]
        self.assertFalse(sudoku.check_solution(grid))

    def test_check_solution_rejects_wrong_dimensions(self):
        self.assertFalse(sudoku.check_solution([]))
        self.assertFalse(sudoku.check_solution([list("123456789")] * 8))
        self.assertFalse(sudoku.check_solution([list("12345678")] * 9))

    def test_generator_boundaries(self):
        for count in (-5, 0, 40, 80, 81, 1000):
            with self.subTest(count=count):
                grid = sudoku.generate_sudoku(count)
                self.assertEqual(9, len(grid))
                self.assertTrue(all(len(row) == 9 for row in grid))
                self.assertEqual(max(0, min(count, 81)), sum(value != "." for row in grid for value in row))
                clues = [row[:] for row in grid]
                solution = sudoku.solve(grid)
                self.assertIsNotNone(solution)
                if solution is not None:
                    self.assertTrue(sudoku.check_solution(solution))
                    for row in range(9):
                        for col in range(9):
                            if clues[row][col] != ".":
                                self.assertEqual(clues[row][col], solution[row][col])

import unittest

class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.board = [
            [0, 0, 2, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 7, 6, 2],
            [4, 3, 0, 0, 0, 0, 8, 0, 0],
            [0, 5, 0, 0, 3, 0, 0, 9, 0],
            [0, 4, 0, 0, 0, 0, 0, 2, 6],
            [0, 0, 0, 4, 6, 7, 0, 0, 0],
            [0, 8, 6, 7, 0, 4, 0, 0, 0],
            [0, 0, 0, 5, 1, 9, 0, 0, 8],
            [1, 7, 0, 0, 0, 6, 0, 0, 5]
        ]
        self.sudoku_board = SudokuBoard(self.board)

    def test_initialization(self):
        self.assertEqual(self.sudoku_board.board, self.board)

    def test_str_representation(self):
        expected_str = (
            "\n╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n"
            "║     |   | 2 ║   |   | 8 ║   |   |   ║\n"
            "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
            "║     |   |   ║   |   | 3 ║ 7 | 6 | 2 ║\n"
            "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
            "║ 4 | 3 |   ║   |   |   ║ 8 |   |   ║\n"
            "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n"
            "║   | 5 |   ║   | 3 |   ║   | 9 |   ║\n"
            "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
            "║   | 4 |   ║   |   |   ║   | 2 | 6 ║\n"
            "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
            "║   |   |   ║ 4 | 6 | 7 ║   |   |   ║\n"
            "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n"
            "║   | 8 | 6 ║ 7 |   | 4 ║   |   |   ║\n"
            "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
            "║     |   |   ║ 5 | 1 | 9 ║   |   | 8 ║\n"
            "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n"
            "║ 1 | 7 |   ║   |   | 6 ║   |   | 5 ║\n"
            "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\n"
        )
        self.assertEqual(str(self.sudoku_board), expected_str)

    def test_find_empty_cell(self):
        self.assertEqual(self.sudoku_board.find_empty_cell(), (0, 0))

    def test_valid_in_row(self):
        self.assertTrue(self.sudoku_board.valid_in_row(0, 1))
        self.assertFalse(self.sudoku_board.valid_in_row(0, 2))

    def test_valid_in_col(self):
        self.assertTrue(self.sudoku_board.valid_in_col(0, 1))
        self.assertFalse(self.sudoku_board.valid_in_col(0, 4))

    def test_valid_in_square(self):
        self.assertTrue(self.sudoku_board.valid_in_square(0, 0, 1))
        self.assertFalse(self.sudoku_board.valid_in_square(0, 0, 2))

    def test_is_valid(self):
        self.assertTrue(self.sudoku_board.is_valid((0, 0), 1))
        self.assertFalse(self.sudoku_board.is_valid((0, 0), 2))

    def test_solver(self):
        solvable_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        unsolvable_board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        sudoku_board_solvable = SudokuBoard(solvable_board)
        sudoku_board_unsolvable = SudokuBoard(unsolvable_board)
        self.assertTrue(sudoku_board_solvable.solver())
        self.assertFalse(sudoku_board_unsolvable.solver())

if __name__ == '__main__':
    unittest.main()

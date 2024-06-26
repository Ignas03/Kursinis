from abc import ABC, abstractmethod
# Abstraction: PuzzleBoard is an abstract base class
class PuzzleBoard(ABC):
    def __init__(self, board):
        # Encapsulation: board is an attribute of the PuzzleBoard class
        self.board = board

    @abstractmethod
    def find_empty_cell(self):
        # Abstraction: Abstract method to be implemented by subclasses
        pass

    @abstractmethod
    def is_valid(self, empty, num):
        # Abstraction: Abstract method to be implemented by subclasses
        pass

    @abstractmethod
    def solver(self):
        # Abstraction: Abstract method to be implemented by subclasses
        pass

    def __str__(self):
        # Encapsulation: String representation of the board
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            row_list = []
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append('║')

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty

            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    @classmethod
    def read_from_file(cls, filename):
        # Encapsulation: Reading the board from a file
        with open(filename, 'r') as file:
            board = []
            for line in file:
                row = [int(num) for num in line.split()]
                board.append(row)
        return cls(board)

    def write_to_file(self, filename):
        # Encapsulation: Writing the board to a file
        with open(filename, 'w') as file:
            for line in self.board:
                file.write(' '.join(str(num) for num in line) + '\n')

# Inheritance: SudokuBoard inherits from PuzzleBoard
class SudokuBoard(PuzzleBoard):
    def find_empty_cell(self):
        # Polymorphism: Specific implementation for Sudoku
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        # Polymorphism: Specific implementation for Sudoku
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Polymorphism: Specific implementation for Sudoku
        return all(
            self.board[row][col] != num
            for row in range(9)
        )

    def valid_in_square(self, row, col, num):
        # Polymorphism: Specific implementation for Sudoku
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # Polymorphism: Specific implementation for Sudoku
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # Polymorphism: Specific implementation for Sudoku
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0

        return False

def solve_sudoku_from_file(input_file, output_file):
    gameboard = SudokuBoard.read_from_file(input_file)
    print(f'\nPuzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)
        gameboard.write_to_file(output_file)
    else:
        print('\nThe provided puzzle is unsolvable.')
    return gameboard

# Example usage
input_file = 'sudoku_input.txt'
output_file = 'sudoku_output.txt'

# Make sure to create 'sudoku_input.txt' with your Sudoku puzzle before running this
solve_sudoku_from_file(input_file, output_file)


  Coursework.Sudoku solver
1. Introduction
   
  What is your application?

Sudoku solver is an aplication that can solve whatever sudoku board you want of course only if it is a solvable board.

  How to run the program?

First of all to run the program you have to create a text input file and output file so it can read from file. Then you need to write a digit matrix which include nine columns and nine rows. And lastly you just run the code and the program will solve the sudoku board.

  How to use the program?

As mentioned in previous step you have to enter the matrix into the input file and run the code

2. Body/Analysis

 4 OOP pillars

  Encapsulation
  
Encapsulation is the bundling of data and methods that operate on that data within a single unit or class. It also involves restricting direct access to some of an object's components.
The SudokuBoard class encapsulates the board data and provides methods to operate on this data, such as find_empty_cell, is_valid, solver, etc.
The PuzzleBoard abstract class provides a general structure for the board and some shared functionality (__str__, read_from_file, write_to_file), encapsulating these details.

class PuzzleBoard(ABC):

    def __init__(self, board):
        self.board = board

    @abstractmethod
    def find_empty_cell(self):
        pass

    @abstractmethod
    def is_valid(self, empty, num):
        pass

    @abstractmethod
    def solver(self):
        pass

    def __str__(self):
        # Implementation for converting board to a string
        pass

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'r') as file:
            board = []
            for line in file:
                row = [int(num) for num in line.split()]
                board.append(row)
        return cls(board)

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for line in self.board:
                file.write(' '.join(str(num) for num in line) + '\n')


  Inheritance
  
Inheritance is a mechanism where a new class inherits the properties and behaviors (methods) of an existing class.
SudokuBoard inherits from PuzzleBoard, gaining access to its attributes and methods. This allows SudokuBoard to use and extend the functionality provided by PuzzleBoard.

class SudokuBoard(PuzzleBoard):

    def find_empty_cell(self):
        # Implementation to find an empty cell
        pass

    def valid_in_row(self, row, num):
        # Implementation to check if a number is valid in a row
        pass

    def valid_in_col(self, col, num):
        # Implementation to check if a number is valid in a column
        pass

    def valid_in_square(self, row, col, num):
        # Implementation to check if a number is valid in a square
        pass

    def is_valid(self, empty, num):
        # Implementation to check if a number is valid
        pass

    def solver(self):
        # Implementation to solve the Sudoku
        pass


  Polymorphism
  
Polymorphism allows methods to do different things based on the object it is acting upon, even though they share the same name.
The find_empty_cell, is_valid, and solver methods in the SudokuBoard class override the abstract methods defined in the PuzzleBoard class. This is an example of polymorphism where the base class defines the method signature and the derived class provides the specific implementation.

class SudokuBoard(PuzzleBoard):

    def find_empty_cell(self):
        # Specific implementation for Sudoku
        pass

    def is_valid(self, empty, num):
        # Specific implementation for Sudoku
        pass

    def solver(self):
        # Specific implementation for Sudoku
        pass


  Abstraction
  
Abstraction involves hiding complex implementation details and showing only the necessary features of an object.
The PuzzleBoard class is an abstract base class (ABC) that defines the interface (find_empty_cell, is_valid, solver) without providing the implementation. This abstract class cannot be instantiated directly and requires subclasses to implement these methods. This provides a template for any type of puzzle board, ensuring they all have certain functionality while allowing specific implementations to vary.

class PuzzleBoard(ABC):

    @abstractmethod
    def find_empty_cell(self):
        pass

    @abstractmethod
    def is_valid(self, empty, num):
        pass

    @abstractmethod
    def solver(self):
        pass


 Design patterns
 
  Template Method Pattern
  
The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method, deferring some steps to subclasses. The pattern lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
In this code, the PuzzleBoard abstract class defines the template for a puzzle board with abstract methods (find_empty_cell, is_valid, solver). The concrete class SudokuBoard implements these methods, providing specific behavior while following the overall structure laid out in the abstract class.

class PuzzleBoard(ABC):

    @abstractmethod
    def find_empty_cell(self):
        pass

    @abstractmethod
    def is_valid(self, empty, num):
        pass

    @abstractmethod
    def solver(self):
        pass

class SudokuBoard(PuzzleBoard):

    def find_empty_cell(self):
        # Implementation for finding an empty cell in Sudoku

    def is_valid(self, empty, num):
        # Implementation for validating a number in Sudoku

    def solver(self):
        # Implementation for solving the Sudoku puzzle
        
  Factory Method Pattern

The Factory Method Pattern is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
In the code, the read_from_file method in the PuzzleBoard class can be seen as a factory method. This method reads the board data from a file and returns an instance of the concrete subclass (SudokuBoard).

class PuzzleBoard(ABC):

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'r') as file:
            board = []
            for line in file:
                row = [int(num) for num in line.split()]
                board.append(row)
        return cls(board)

class SudokuBoard(PuzzleBoard):
    pass
    
 Reading from file and writing to file

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

3. Conlusion
   
   So dificulties that has been faced during this coursework was to implement all four OOP pillars while writing this code but in the end the purpose of this coursework was achieved.




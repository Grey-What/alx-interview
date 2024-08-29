#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""
import sys


def generate_solutions(row, column):
    """
    Generates all possible solutions for placing N queens on an NxN chessboard.

    Parameters:
        row (int): The number of rows on the chessboard.
        column (int): The number of columns on the chessboard.

    Returns:
        list: A list of all possible solutions,
            where each solution is a list of column indices for each queen.
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Generates all possible safe positions for a queen on a chessboard.

    Parameters:
        queen (int): The row index of the queen.
        column (int): The number of columns on the chessboard.
        prev_solution (list):
          A list of lists representing the current state of the board.

    Returns:
        list: A list of lists representing all
          possible safe positions for the queen.
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    Checks if it is safe to place a queen at position (q, x) on the board.

    Parameters:
    q (int): The row index of the queen.
    x (int): The column index of the queen.
    array (list): The current state of the board,
         represented as a list of column indices.

    Returns:
    bool: True if it is safe to place the queen, False otherwise.
    """
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Initializes the nqueens program by validating the command line argument.

    The function checks if the correct number of arguments is provided,
    if the argument is a digit, and if the number is at least 4.
    If any of these conditions are not met,
      it prints an error message and exits.

    Returns:
        int: The value of N if all conditions are met.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    """
    Solves the N queens problem by generating all possible solutions
      for a given board size.

    Parameters:
    None

    Returns:
    None
    """
    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()

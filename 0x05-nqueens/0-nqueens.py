#!/usr/bin/python3
"""
0-nqueens.py
Solves the N Queens puzzle.
Usage: nqueens N
Prints all possible solutions to the N Queens problem for a given N.
"""
import sys

def is_safe(queens, row, col):
    """
    Checks if a queen can be placed at (row, col) safely.
    queens: list of placed queens as [row, col]
    row: current row to check
    col: current column to check
    Returns: True if safe, False otherwise
    """
    for q_row, q_col in queens:
        if col == q_col or abs(row - q_row) == abs(col - q_col):
            return False
    return True

def solve_nqueens(n, row, queens, solutions):
    """
    Recursively attempts to solve the N Queens problem.
    n: size of the board (N)
    row: current row to place a queen
    queens: list of currently placed queens
    solutions: list to store all the valid solutions
    """
    if row == n:
        solutions.append([q[:] for q in queens])
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()

def main():
    """
    Main entry point, parses arguments and prints solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

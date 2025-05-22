#!/usr/bin/python3
"""
Solves the N Queens problem using backtracking.
Usage: nqueens N
Prints all solutions for placing N non-attacking queens on an N×N chessboard.
"""
import sys

def print_solutions(solutions):
    for sol in solutions:
        print(sol)

def is_safe(row, col, solution):
    for r, c in solution:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def solve_nqueens(N, row=0, solution=[], solutions=[]):
    if row == N:
        solutions.append([pos[:] for pos in solution])
        return
    for col in range(N):
        if is_safe(row, col, solution):
            solution.append([row, col])
            solve_nqueens(N, row + 1, solution, solutions)
            solution.pop()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N, 0, [], solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()

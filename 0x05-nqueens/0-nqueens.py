#!/usr/bin/python3
"""
Solution to the N Queens problem.
"""
import sys


def backtrack(row, n, cols, pos_diags, neg_diags, board):
    """
    Recursively places queens on the board and prints solutions.

    Args:
        row (int): current row to place the queen
        n (int): size of the board (number of queens)
        cols (set): set of occupied columns
        pos_diags (set): set of occupied positive diagonals (r + c)
        neg_diags (set): set of occupied negative diagonals (r - c)
        board (list): current state of the board (2D list)
    """
    if row == n:
        res = []
        for r in range(n):
            for c in range(n):
                if board[r][c] == 1:
                    res.append([r, c])
        print(res)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
            continue

        cols.add(col)
        pos_diags.add(row + col)
        neg_diags.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diags, neg_diags, board)

        cols.remove(col)
        pos_diags.remove(row + col)
        neg_diags.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Initializes and starts the backtracking process.

    Args:
        n (int): Number of queens (size of board)
    """
    cols = set()
    pos_diags = set()
    neg_diags = set()
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(0, n, cols, pos_diags, neg_diags, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(N)

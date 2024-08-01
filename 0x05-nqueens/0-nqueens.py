#!/usr/bin/python3
"""
place N non-attacking queens on an N×N chessboard
"""

import sys


def solve_nqueens(row, n, cols, pos_diags, neg_diags, board):
    """
    Recursively solves the N-Queens problem
    """
    if row == n:
        solution = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    for col in range(n):
        if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
            continue

        cols.add(col)
        pos_diags.add(row + col)
        neg_diags.add(row - col)
        board[row][col] = 1

        solve_nqueens(row + 1, n, cols, pos_diags, neg_diags, board)

        cols.remove(col)
        pos_diags.remove(row + col)
        neg_diags.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    function to solve the problem
    """
    columns = set()
    positive_diagonals = set()
    negative_diagonals = set()
    chess_board = [[0] * n for _ in range(n)]

    solve_nqueens(0, n, columns, positive_diagonals,
                  negative_diagonals, chess_board)


if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num_queens = int(arguments[1])
        if num_queens < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(num_queens)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

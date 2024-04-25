#!/usr/bin/python3


def main(argv):

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(argv[1])

    if n < 4:
        print("N must be at least 4")
        exit(1)

    # board represented by columns of int
    # int is the row number the queen is at
    board = [0 for _ in range(n)]
    return find_solutions(board, 0, n)


def find_solutions(board, col, size):
    # Board is full, end recursion, print solution
    if col >= size:
        print_board(board, size)
        return True

    for row in range(size):
        if is_safe(board, row, col):
            board[col] = row
            find_solutions(board, col + 1, size)

    return False


def is_safe(board, row, col):
    for c in range(col):
        # Check left of current
        if board[c] == row:
            return False
        # Check upper left diagonal
        if board[c] - (col - c) == row:
            return False
        # Check lower left diagonal
        if board[c] + (col - c) == row:
            return False
    return True


def print_board(board, size):
    # Print x y coordinates of the queens
    print(str([[col, board[col]] for col in range(size)]))


if __name__ == "__main__":
    import sys

    main(sys.argv)

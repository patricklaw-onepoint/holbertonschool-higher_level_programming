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

    if not find_all_solutions(n):
        print("Solution does not exist")


def find_all_solutions(n):
    found = False
    for i in range(n):
        board = [[False] * n for _ in range(n)]
        if find_solutions(board, 0, n, i):
            print_board(board, n)
            found = True

    return found


def find_solutions(board, col, n, starting_pos):
    # Board is full, end recursion
    if col >= n:
        return True

    for row in range(n):
        if col == 0 and row <= starting_pos:
            # Shift starting position to get the next solution.
            continue
        if is_safe(board, row, col, n):
            # Try place queens into rows, remove queen if not safe and try next.
            board[row][col] = True
            if find_solutions(board, col + 1, n, starting_pos):
                return True
            board[row][col] = False

    return False


def is_safe(board, row, col, n):
    # Check left of current
    if any(board[row][i] for i in range(col)):
        return False

    # Check upper left diagonal
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check lower left diagonal
    if any(board[i][j] for i, j in zip(range(row, n, 1), range(col, -1, -1))):
        return False

    return True


def print_board(board, n):
    # Print after converting board to coordinates
    print([[i, j] for i in range(n) for j in range(n) if board[i][j]])


if __name__ == "__main__":
    import sys

    main(sys.argv)

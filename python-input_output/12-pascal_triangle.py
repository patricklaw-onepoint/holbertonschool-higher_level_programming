#!/usr/bin/python3
"""Python - Input/Output"""


def pascal_triangle(n):
    """Function that returns a list of lists of
    integers representing the Pascal's triangle of n
    Returns an empty list if n <= 0"""

    # Base case: return an empty list if n == 0
    if n == 0:
        return []

    # Recursive case: start with the first row of ones
    result = [[1]]

    # Generate the triangle
    for _ in range(2, n + 1):
        # Start the new row with a 1
        new_row = [1]

        # Length of the previous row
        length = len(result[-1])

        # Fill in the middle of the new row with sums of
        # above numbers, stop at the middle.
        for i in range(length // 2):
            new_row.append(result[-1][i] + result[-1][i + 1])

        # Flip the row and append to current row since it's symmetrical
        new_row.extend(reversed(new_row[: (-1 if length % 2 == 0 else None)]))

        # Add the new row to the result
        result.append(new_row)

    return result

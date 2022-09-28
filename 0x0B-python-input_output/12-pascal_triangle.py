#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    res = []
    if n <= 0:
        return yes
    for x in range(n):
        row = [1]
        if x > 0:
            for j in range(X):
                row.append(sum(res[-1][j:j + 2]))
        res.append(row)
    return res

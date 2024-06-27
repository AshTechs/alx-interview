#!/usr/bin/python3
"""
Defines a class PascalTriangle to generate Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list of lists: Pascal's Triangle as a list of lists of integers.
    """
    triangle = []

    if n <= 0:
        return triangle

    # Generate first row
    triangle.append([1])

    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle


# Example usage:
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Prints the Pascal's Triangle.

        Args:
            Pascal's Triangle represented as a list of lists of integers
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

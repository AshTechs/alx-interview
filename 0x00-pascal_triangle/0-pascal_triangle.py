#!/usr/bin/python3
"""
Defines a class PascalTriangle to generate Pascal's Triangle up to n rows.
"""

class PascalTriangle:
    """Represents Pascal's Triangle up to n rows."""

    def __init__(self, n):
        """Initializes Pascal's Triangle with up to n rows.

        Args:
            n (int): Number of rows to generate.
        """
        self.n = n

    @property
    def n(self):
        """Gets/Sets the number of rows in Pascal's Triangle."""
        return self.__n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            raise TypeError("n must be an integer")
        elif value <= 0:
            raise ValueError("n must be greater than 0")
        self.__n = value

    def generate_triangle(self):
        """Generates Pascal's Triangle up to n rows."""
        triangle = []

        for i in range(self.n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle

    def print_triangle(self):
        """Prints Pascal's Triangle."""
        triangle = self.generate_triangle()
        for row in triangle:
            print(" ".join(map(str, row)).center(self.n * 3))

# Example usage:
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of rows for Pascal's Triangle: "))
        pt = PascalTriangle(n)
        pt.print_triangle()
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid integer greater than 0.")

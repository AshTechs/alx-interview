#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid: 2D grid representing the map, where 1 is land and 0 is water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check up (r-1)
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check down (r+1)
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check left (c-1)
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check right (c+1)
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter

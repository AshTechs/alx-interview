#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes: A list of lists where each sublist contains keys to other boxes

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    if n == 0:
        return False

    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)


if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))

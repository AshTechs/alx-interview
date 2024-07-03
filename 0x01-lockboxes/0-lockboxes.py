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
    opened = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in opened and key < n:
                opened.add(key)
                stack.append(key)

    return len(opened) == n

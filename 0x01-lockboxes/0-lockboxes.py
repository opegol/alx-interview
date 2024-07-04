#!/usr/bin/python3

"""Method that determines if all boxes (represented as list of lists
   of numbers denoting keys that may open other similarly numbered
   boxes) can be opened.

    A key with the same number as a box opens that box
    Assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
"""


def canUnlockAll(boxes):
    """Function to check if all boxes can be opened

    Args:
        boxes (list): this is a list of lists of numbers
    Return:
        True if all boxes can be opened, else return False
        if not boxes: return False
    """

    n = len(boxes)
    if n == 0:
        return True

    # List to keep track of opened boxes
    opened = [False] * n
    opened[0] = True  # Start with the first box opened

    # List to act as queue for BFS
    queue = [0]
    front = 0

    while front < len(queue):
        box = queue[front]
        front += 1

        # Check keys in the current box
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    # If we have opened all boxes
    return all(opened)

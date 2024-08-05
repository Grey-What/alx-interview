#!/usr/bin/python3
"""solving lockboxes"""


def canUnlockAll(boxes):
    """
    determines if all the boxes in a list of boxes
    contains the indices to other boxes
    """

    unlocked = [0]
    for box in unlocked:
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    return len(unlocked) == len(boxes)

#!/usr/bin/python3
"""Method that determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Function that determines if all boxes can be unlocked
    Args:
        boxes: list of lists containing keys
    Returns:
        True if all boxes can be unlocked, False otherwise
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()

        if not boxIdx or boxIdx >= n:
            continue

        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    return n == len(seen_boxes)

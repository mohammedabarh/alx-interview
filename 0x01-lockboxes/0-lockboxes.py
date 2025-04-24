#!/usr/bin/python3
"""
Module for the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    Args:
        boxes (list): List of lists where each inner list contains keys
    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return True

    # Set to keep track of boxes we can open
    unlocked = {0}
    # Set to keep track of new keys we find
    keys = set(boxes[0])

    # While we keep finding new keys
    while keys:
        # Get a key from our set of keys
        key = keys.pop()
        
        # If this key opens a new box (key is valid and box not yet unlocked)
        if key < n and key not in unlocked:
            # Add this box to our unlocked set
            unlocked.add(key)
            # Add all keys from this box to our keys set
            keys.update(boxes[key])

    # Return True if we could unlock all boxes, False otherwise
    return len(unlocked) == n

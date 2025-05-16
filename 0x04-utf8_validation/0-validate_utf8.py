#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    
    Args:
        data: List of integers representing 1 byte of data each
        
    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks for checking UTF-8 bytes
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get only the 8 least significant bits
        byte = num & 255

        if n_bytes == 0:
            # Count number of most significant bits set to 1
            mask = 1 << 7
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            # Check if byte starts with 10
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # Check if all characters were complete
    return n_bytes == 0

#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): List of integers where each integer represents 1 byte of data
        
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    # Counter for remaining bytes in current character
    remaining_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Get only the 8 least significant bits
        byte = byte & 0xFF

        # If we're not currently in a multi-byte sequence
        if remaining_bytes == 0:
            # Count leading 1s to determine bytes in sequence
            if byte >> 7 == 0:  # 1 byte character (0xxxxxxx)
                remaining_bytes = 0
            elif byte >> 5 == 0b110:  # 2 byte character (110xxxxx)
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:  # 3 byte character (1110xxxx)
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:  # 4 byte character (11110xxx)
                remaining_bytes = 3
            else:  # Invalid starting byte
                return False
        else:
            # Check if byte is a valid continuation byte (10xxxxxx)
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1

    # Check if all characters were complete
    return remaining_bytes == 0

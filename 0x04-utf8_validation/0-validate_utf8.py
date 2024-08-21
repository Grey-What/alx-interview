#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """
    determines if a given data set
    represents a valid UTF-8 encoding

    Returns: True if data is a valid UTF-8 encoding, else False

    Args: data (list): a list of integers
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0

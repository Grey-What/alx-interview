#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """
    determines if a given data set
    represents a valid UTF-8 encoding

    Returns: True if data is a valid UTF-8 encoding, else False

    Args: data (list): a list of integers
    """
    continue_bytes = 0

    # bit pattern
    UTF8_BIT_1 = 1 << 7
    UTF8_BIT_2 = 1 << 6

    for byte in data:
        one_mask = 1 << 7

        if continue_bytes == 0:

            while one_mask & byte:
                continue_bytes += 1
                one_mask = one_mask >> 1

            if continue_bytes == 0:
                continue

            if continue_bytes == 1 or continue_bytes > 4:
                return False
        else:
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

            continue_bytes -= 1

    if continue_bytes != 0:
        return False
    return True

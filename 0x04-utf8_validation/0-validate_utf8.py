#!/usr/bin/env python3
"""
UTF-validation
"""


def validUTF8(data):
    """
    method that determines if a given data set 
    represents a valid UTF-8 encoding
    """
    byte_count = 0

    for num in data:
        mask = 1 << 7
        if not byte_count:
            while mask & num:
                byte_count += 1
                mask >>= 1

            if byte_count == 0:
                continue

            if byte_count == 1 or byte_count > 4:
                return False
        else:
            if not (num & 1 << 7 and not (num & 1 << 6)):
                return False
        byte_count -= 1
    return byte_count == 0


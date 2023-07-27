#!/usr/bin/env python3
"""
UTF-validation
"""


def validUTF8(data):
    """
    method that determines if a given data set 
    represents a valid UTF-8 encoding
    """
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        mask_n = 1 << 7
        if n_bytes == 0:
            while mask_n & num:
                n_bytes += 1
                mask_n = mask_n >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0

#!/usr/bin/env python3
"""Log Parsing"""


import sys


def print_stats(file_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{}: {}".format(key, value))

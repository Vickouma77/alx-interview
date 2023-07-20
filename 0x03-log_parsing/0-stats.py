#!/usr/bin/env python3
"""Log Parsing"""


import random
import sys
from time import sleep


def print_msg(total_size, status_codes):
    """Prints the log parsing stats"""
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            input_list = line.split()
            if len(input_list) > 2:
                total_size += int(input_list[-1])
                if input_list[-2] in status_codes:
                    status_codes[input_list[-2]] += 1
            if counter % 10 == 0:
                print_msg(total_size, status_codes)
        print_msg(total_size, status_codes)
    except KeyboardInterrupt:
        print_msg(total_size, status_codes)
        raise
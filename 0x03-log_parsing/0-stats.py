#!/usr/bin/env python3
"""Log Parsing"""


import sys


def print_stats(file_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            try:
                file_size += int(data[-1])
            except:
                pass
            try:
                if data[-2] in status_codes:
                    status_codes[data[-2]] += 1
            except:
                pass
            if counter % 10 == 0:
                print_stats(file_size, status_codes)
        print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

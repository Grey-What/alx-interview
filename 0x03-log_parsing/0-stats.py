#!/usr/bin/python3
"""parses a HTTP request log file"""
import sys


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}
size = 0
counter = 0

try:
    for line in sys.stdin:
        l_list = line.split(" ")

        if len(l_list) > 4:
            try:
                status_code = l_list[-2]
                file_size = int(l_list[-1])

                if status_code in status_codes.keys():
                    status_codes[status_code] += 1

                size += file_size
                counter += 1
            except (IndexError, ValueError) as e:
                continue

    if counter == 10:
        print("File size: {}".format(size))
        for k, v in sorted(status_codes.items()):
            if v != 0:
                print("{}: {}".format(k, v))
        counter = 0

except Exception as err:
    pass

finally:
    print("File size: {}".format(size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))
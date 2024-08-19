#!/usr/bin/python3
"""parses a HTTP request log file"""

import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}


total_size = 0
count = 0

try:
    for line in sys.stdin:
        lines_list = line.split(" ")

        if len(lines_list) > 4:
            status_code = lines_list[-2]
            file_size = int(lines_list[-1])

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += file_size
            count += 1

        if count == 10:
            count = 0
            print("File size: {}".format(total_size))

            for k, v in sorted(status_codes.items()):
                if v != 0:
                    print("{}: {}".format(k, v))

except Exception as e:
    pass

finally:
    print("File size: {}".format(total_size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))

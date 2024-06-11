#!/usr/bin/python3
"""Python - Input/Output"""

# Script that reads stdin line by line and computes metrics:

# Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
# Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
#   Total file size: File size: <total size>
#   where is the sum of all previous (see input format above)
#   Number of lines by status code:
#       possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
#       if a status code doesn’t appear, don’t print anything for this status code
#       format: <status code>: <number>
#       status codes should be printed in ascending order

"""
77.209.146.200 - [2024-06-11 18:16:21.751878] "GET /projects/260 HTTP/1.1" 401 138
41.48.115.168 - [2024-06-11 18:16:21.751878] "GET /projects/260 HTTP/1.1" 200 876
43.28.89.224 - [2024-06-11 18:16:21.752874] "GET /projects/260 HTTP/1.1" 404 452
51.200.24.137 - [2024-06-11 18:16:21.752874] "GET /projects/260 HTTP/1.1" 301 7
118.238.136.108 - [2024-06-11 18:16:21.752874] "GET /projects/260 HTTP/1.1" 404 715
146.218.5.190 - [2024-06-11 18:16:21.753872] "GET /projects/260 HTTP/1.1" 500 368
240.170.150.152 - [2024-06-11 18:16:21.753872] "GET /projects/260 HTTP/1.1" 405 69
118.93.9.43 - [2024-06-11 18:16:21.753872] "GET /projects/260 HTTP/1.1" 403 519
107.120.22.200 - [2024-06-11 18:16:21.753872] "GET /projects/260 HTTP/1.1" 403 344
102.217.66.220 - [2024-06-11 18:16:21.754992] "GET /projects/260 HTTP/1.1" 404 148
"""

import sys

if __name__ == "__main__":
    total_size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def parse_line(line):
        try:
            _, code_str, size_str = line.rsplit(maxsplit=2)
            total_size[0] += int(size_str)
            code = int(code_str)
            codes[code] = codes.get(code, 0) + 1
        except ValueError:
            pass

    def print_stats():
        print(f"File size: {total_size[0]}")
        for code, count in sorted(codes.items()):
            if count > 0:
                print(f"{code}: {count}")

    i = 0

    try:
        for line in sys.stdin:
            parse_line(line)
            i += 1
            if i % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys
import re


def print_stats(total_size, status_codes):
    """
    Print accumulated statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def validate_line(line):
    """
    Validate if a line matches the expected format using regex
    Returns status_code and file_size if valid, None otherwise
    """
    pattern = r'^[\d\.]+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line.strip())
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        return status_code, file_size
    return None


def main():
    """
    Main function to process the logs
    """
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            result = validate_line(line)
            
            if result:
                status_code, file_size = result
                
                # Update metrics only if status code is valid
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

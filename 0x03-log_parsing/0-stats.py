#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""


import sys


def print_metrics(file_size, status_codes):
    """
    Print accumulated metrics.
    Args:
        file_size: Total file size
        status_codes: Dictionary of status codes and their counts
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def process_line(line, status_codes):
    """
    Process a single line and extract status code and file size.
    Args:
        line: Input line to process
        status_codes: Dictionary of status codes
    Returns:
        file_size: Size from the line, or 0 if invalid
    """
    try:
        parts = line.split()
        # Check if line has enough parts
        if len(parts) < 2:
            return 0

        # Get file size from last element
        file_size = int(parts[-1])

        # Get status code from second to last element
        status_code = int(parts[-2])

        # Update status code count if it's valid
        if status_code in status_codes:
            status_codes[status_code] += 1

        return file_size

    except (IndexError, ValueError):
        return 0


def main():
    """
    Main function to process stdin and compute metrics.
    """
    total_file_size = 0
    line_count = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            total_file_size += process_line(line, status_codes)

            if line_count % 10 == 0:
                print_metrics(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_codes)
        raise

    print_metrics(total_file_size, status_codes)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_codes):
    """
    Print the statistics
    Args:
        total_size: Total file size
        status_codes: Dictionary of status codes and their counts
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Main function to process the logs
    """
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                # Split the line and extract relevant parts
                parts = line.split()
                if len(parts) < 7:
                    continue

                # Get status code and file size
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update metrics
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

            except (ValueError, IndexError):
                # Skip lines that don't match the expected format
                continue

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_stats(total_size, status_codes)
        raise

    # Print final stats if the input ends normally
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

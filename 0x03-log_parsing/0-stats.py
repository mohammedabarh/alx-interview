#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""


import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print statistics
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key in sorted(dict_sc.keys()):
        if dict_sc[key] != 0:
            print("{}: {}".format(key, dict_sc[key]))


def main():
    """
    Main function to process stdin and compute metrics
    """
    total_file_size = 0
    counter = 0
    dict_sc = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        for line in sys.stdin:
            try:
                # Split and reverse the line
                parsed_line = line.split()
                parsed_line = parsed_line[::-1]

                if len(parsed_line) > 2:
                    counter += 1

                    # Get file size
                    total_file_size += int(parsed_line[0])

                    # Get status code
                    status_code = parsed_line[1]
                    if status_code in dict_sc:
                        dict_sc[status_code] += 1

                    # Print every 10 lines
                    if counter == 10:
                        print_msg(dict_sc, total_file_size)
                        counter = 0

            except (IndexError, ValueError):
                continue

    except KeyboardInterrupt:
        print_msg(dict_sc, total_file_size)
        sys.exit(0)

    print_msg(dict_sc, total_file_size)


if __name__ == "__main__":
    main()

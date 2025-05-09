#!/usr/bin/python3
import sys
import re
import signal

# Initialize metrics
total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

# Regular expression pattern to match log lines
log_pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)

def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interrupt (CTRL+C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            
            # Update metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            
            line_count += 1
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()
except Exception:
    pass
finally:
    # Print stats at the end in case of any termination
    print_stats()

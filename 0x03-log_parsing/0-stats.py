#!/usr/bin/python3
"""
Log parser module
"""
import sys
import signal

# Dictionary to store the count of status codes
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Variable to store the total file size
total_file_size = 0

# Line counter
line_count = 0


def print_stats():
    """Print the collected statistics."""
    global total_file_size, status_code_counts
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        # Check if line matches the expected format
        if len(parts) != 10 or parts[2] != '"GET' or parts[3] != '/projects/260' or parts[4] != 'HTTP/1.1"':
            continue

        try:
            status_code = int(parts[5])
            file_size = int(parts[6])
        except ValueError:
            continue

        # Increment the appropriate status code count
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Add to the total file size
        total_file_size += file_size

        # Increment the line counter
        line_count += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
finally:
    print_stats()

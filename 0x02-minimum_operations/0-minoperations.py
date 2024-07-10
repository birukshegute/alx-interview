#!/usr/bin/env python3
"""
performs minOperations(n) function
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    next = 'H'
    file = 'H'
    operations = 0
    while (len(file) < n):
        if n % len(file) == 0:
            operations += 2
            next = file
            file += file
        else:
            operations += 1
            file += next
    if len(file) != n:
        return 0
    return operations

#!/usr/bin/python3
"""
performs minOperations(n) function
"""


def minOperations(n):
    """
    calculates the fewest number of operations to result n H characters.
    """
    next = 'H'
    file = 'H'
    operations = 0
    if n <= 1:
        return 0
    while (len(file) < n):
        if n % len(file) == 0:
            operations += 2
            next = file
            file += file
        else:
            operations += 1
            file += next
    return operations

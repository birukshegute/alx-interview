#!/usr/bin/python3
"""
performs minOperations(n) function
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations to result n H characters.
    """
    next: str = 'H'
    file: str  = 'H'
    operations: int = 0
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

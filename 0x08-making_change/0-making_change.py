#!/usr/bin/python3
"""
Algorithm to make changes
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    elif total > 0:
        arr = sorted(coins[:])
        arr = list(reversed(arr))
        count = 0
        value = total + 0
        index = 0
        while value >= 0 and (index < len(arr)):
            if value >= arr[index]:
                value = value - arr[index]
                count += 1
            elif value < arr[index]:
                index += 1
        if index == len(arr):
            if value != 0:
                return -1
            elif value == 0:
                return count

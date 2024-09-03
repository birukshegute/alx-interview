#!/usr/bin/python3
"""Module to do the task."""


def isWinner(x, nums):
    """Function to handle the task"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    benWins = 0
    mariaWins = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1
    if benWins > mariaWins:
        return "Ben"
    if mariaWins > benWins:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """Removes multiples of primes"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break

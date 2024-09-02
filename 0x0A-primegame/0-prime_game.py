#!/usr/bin/python3
"""Module to do the task."""


def isWinner(x, nums):
    """Function to handle the task"""
    mariaWins = 0
    benWins = 0

    for num in nums:
        rounds = list(range(1, num + 1))
        primes = primes_in_range(1, num)

        if not primes:
            benWins += 1
            continue

        isMariaTurns = True

        while(True):
            if not primes:
                if isMariaTurns:
                    benWins += 1
                else:
                    mariaWins += 1
                break

            smallestPrime = primes.pop(0)
            rounds.remove(smallestPrime)

            rounds = [x for x in rounds if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

    if mariaWins > benWins:
        return "Maria"

    if mariaWins < benWins:
        return "Ben"

    return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end+1) if is_prime(n)]
    return primes

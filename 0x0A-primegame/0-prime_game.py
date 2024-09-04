#!/usr/bin/python3
"""Playing a Prime Game.
"""


def soePrimes(n):
    """Return list of prime numbers between 1 and n inclusive
        using Sieve of Eratosthenes.
    """
    primeArr = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (primeArr[p]):
            for i in range(p * p, n + 1, p):
                primeArr[i] = False
        p += 1
    primes = [i for i in range(2, n + 1) if primeArr[i]]
    return primes


def isWinner(x, nums):
    """
    Returns the winner of a Prime Game
    Args:
        x (int): no. of rounds of prime game
        nums (int): array of upper bound n of each round where n is a set of
                consecutive integers starting from 1 up to and including n
    Return:
        Name of player (Maria or Ben) that wins the most rounds or
        None if winner cannot be determined.
    """
    Maria = 0
    Ben = 0
    for i in range(x):
        primes = soePrimes(nums[i])
        if len(primes) % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    else:
        return "Ben" if Ben > Maria else "Maria"

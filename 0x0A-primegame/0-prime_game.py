#!/usr/bin/python3
"""Playing a Prime Game.
"""


def soePrimes(n):
    """Return list of prime numbers between 1 and n inclusive
        using Sieve of Eratosthenes.
    """
    primeArr = [True] * (n + 1)
    primeArr[0] = primeArr[1] = False
    p = 2
    while (p * p <= n):
        if (primeArr[p]):
            for i in range(p * p, n + 1, p):
                primeArr[i] = False
        p += 1
    primes = [i for i in range(2, n + 1) if primeArr[i]]
    return primes
    
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos
    """

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
    
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        primes = soePrimes(nums[i])
        # print(primes)
        if len(primes) % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    else:
        return "Ben" if Ben > Maria else "Maria"
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = soePrimes(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None

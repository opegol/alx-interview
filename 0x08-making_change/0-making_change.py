#!/usr/bin/python3
"""Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
"""
import sys


def helpChange(coins, n, total, tab):
    """Helper function for minimum change problem"""
    if (total <= 0):
        return 0

    if tab[total] != -1:
        return tab[total]

    count = sys.maxsize

    for i in range(n):
        if (coins[i] <= total):
            sub_count = helpChange(coins, n, total - coins[i], tab)
            if (sub_count != sys.maxsize and sub_count + 1 < count):
                count = sub_count + 1
    tab[total] = count

    return count


def makeChange1(coins, total):
    """Return the fewest number of coins needed to meet total."""
    n = len(coins)
    tab = [-1] * (total + 1)

    ret = helpChange(coins, n, total, tab)
    if ret == sys.maxsize:
        return -1
    return ret


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total."""

    if total <= 0:
        return 0

    else:
        coins.sort(reverse=True)
        count = 0
        for n in coins:
            while (total >= n):
                total -= n
                count += 1
        if total == 0:
            return count
        return -1

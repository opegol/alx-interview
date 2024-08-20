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
    """This function will take a list of coins and use
       that to calculate how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1

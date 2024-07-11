#!/usr/bin/python3

"""Method to devise a solution that efficiently calculates
   the minimum number of operations to achieve a given number
   of characters using only “Copy All” and “Paste” operations. 
"""


def minOperations(n):
"""calculates the fewest number of operations"""
    ops = 0
    current = 1 # current number of Hs in the file
    counter = 0
    
    while now < n:
        rem = n - current 
        if (rem % current == 0):
            ops = current
            current += ops
            counter += 2
        else:
            current += ops
            counter += 1
    return counter

def minOperations(n):
    if n <= 1:
        return 0
    
    ops = 0
    current = 1  # current number of Hs in the file
    
    for d in range(2, n + 1):
        while n % d == 0:
            ops += d
            n //= d
            current *= d
    
    if n > 1:
        return 0  # If we have remainder left, n wasn't completely factorized to 1
    
    return ops
  

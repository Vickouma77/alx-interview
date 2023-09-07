#!/usr/bin/env python3
"""Prime Game"""

def isWinner(x, nums):
    """
    Determines winner of prime game
    args:
        x: number of rounds
        nums: array of n
    Returns:
        Name of the player that won the most rounds
        If the winner cannot be determined, return None
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    sieve = [i for i, prime in enumerate(sieve) if prime]
    c = 0
    for n in nums:
        for prime in sieve:
            if prime <= n:
                c += 1
        if c % 2 == 0:
            return "Maria"
        else:
            return "Ben"

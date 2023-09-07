#!/usr/bin/env python3
"""Prime Game"""


def primes(n):
    """
    Generates prime numbers
    args:
        n: number
    Returns:
        list of prime numbers
    """
    prime = []
    for i in range(1, n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime.append(i)
    return prime

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
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None

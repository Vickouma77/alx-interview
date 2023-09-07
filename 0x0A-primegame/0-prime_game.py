#!/usr/bin/env python3
"""Prime Game"""

def isWinner(x, nums):
    """
    Pime Game function to know who is the winner of the game 
    based on the number of rounds and the list of integers
    x: number of rounds to play 
    nums: an array of n number of integers
    Return: name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for i in range(n + 1)]
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    c = 0
    for i in range(len(sieve)):
        if sieve[i] == True:
            c += 1
        sieve[i] = c
    player1 = 0
    for n in nums:
        player1 += sieve[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
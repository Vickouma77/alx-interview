#!/usr/bin/env python3
"""Change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    i = 0
    num_coins = 0
    while (total > 0 and i < len(coins)):
        if (total - coins[i]) >= 0:
            total -= coins[i]
            num_coins += 1
        else:
            i += 1
    if total != 0:
        return -1
    return num_coins

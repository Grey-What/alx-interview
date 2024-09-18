#!/usr/bin/python3
"""
Interview Task: 0x08. Making Change
fewest number of coins needed to meet a give total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        while total >= coin:
            total -= coin
            count += 1
    if total > 0:
        return -1
    return count

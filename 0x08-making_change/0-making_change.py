#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Args:
    coins ([list]): a list of the values of the coins in your possession
    total ([number]): amount
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, n_coins = (0, 0)
    cpy_total = total
    len_coins = len(coins)

    while(i < len_coins and cpy_total > 0):
        if (cpy_total - coins[i]) >= 0:
            cpy_total -= coins[i]
            n_coins += 1
        else:
            i += 1

    check = cpy_total > 0 and n_coins > 0
    return -1 if check or n_coins == 0 else n_coins

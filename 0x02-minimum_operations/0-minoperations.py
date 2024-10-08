#!/usr/bin/python3
"""
Minimum number of operations nedded to rach a number of characters

n a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """

    if not isinstance(n, int) or n < 1:
        return 0

    ops_count = 0
    total_H = 1

    while n > 1:
        for i in range(2, n + 1):
            while n % i == 0:
                ops_count += i
                n = n // i

    return ops_count

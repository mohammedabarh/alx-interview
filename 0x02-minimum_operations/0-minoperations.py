#!/usr/bin/python3
"""
Module that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): The target number of H characters

    Returns:
        int: The minimum number of operations needed.
             Returns 0 if n is impossible to achieve.
    """
    # If n is less than or equal to 1, return 0
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Continue until n is fully factorized
    while n > 1:
        # If n is divisible by the current divisor
        while n % divisor == 0:
            # Add the divisor to operations
            operations += divisor
            # Divide n by the divisor
            n = n // divisor
        # Increment divisor to try next number
        divisor += 1

        # Optimization: if divisor squared is greater than n
        # and n is greater than 1, then n is prime
        if divisor * divisor > n and n > 1:
            operations += n
            break

    return operations

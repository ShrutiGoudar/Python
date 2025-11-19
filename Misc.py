import os
import logging

def fibonacci(n):
    #return a list of fibonnaci series of lenght n
    logger = logging.getLogger(__name__)
    logger.info(f"Generating Fibonacci series of length {n}")
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-2] + fib[i-1])
    return fib


def count_digits(n):
    """ count_digits () :
    Count the number of digits in a positive integer.
    Args:
        n (int): A positive integer
    Returns:
        int: Number of digits in n
    """
    # Input validation
    if not isinstance(n, int):
        return None
    #Handles negative number
    if n < 0: 
        n = abs(n)
    # Handle zero case
    if n == 0:
        return 1
  
    count = 0
    while n > 0:
        count += 1
        n //= 10  # More Pythonic than n = n // 10
    
    return count
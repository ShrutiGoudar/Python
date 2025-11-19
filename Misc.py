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
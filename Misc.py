import os
import logging
from functools import wraps

def log_calls(func):
    @wraps(func)        #this preserves metadata of func
    def wrapper(*args, **kwargs ):
        print (f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        res = func(*args, **kwargs)
        print(f"{func.__name__} returned: {res}")
        return res
    return wrapper   

@log_calls      # Example of decorator 
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

def check_palindrome_numer(n: int) ->bool:
    num_of_digits = count_digits(n)
    copy_of_num = n
    rev =0
    while copy_of_num:
        rev = rev*10 + copy_of_num%10
        copy_of_num //=10
    return n == rev

#Basic version
def check_palindrome(str_name):
    comp_val = str_name.lower()
    return comp_val == comp_val[::-1]
    
# Refined version : clean code
def is_palindrome(s: str) -> bool:
    if isinstance(s, str):
        return check_palindrome(s)
    elif isinstance(s, int):
        return check_palindrome_numer(s)

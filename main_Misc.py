import Misc

def main():
    """ 1. Fibonacci
    n = int(input("Enter length of Fibonnaci series: "))
    print(Misc.fibonacci(n)) """
    """ 2. Count digits
    res = Misc.count_digits(34)
    print(f"{res} " if res is not None else "Not a number")
    """
    
    #3. Check paliandrome
    if Misc.is_palindrome("123ab321"):
        print ("It is a Palindrome")
    else :
        print("Not a paliandrome")

   
   
    

if __name__ == "__main__":
    main()

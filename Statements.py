#1: Print first 10 natural numbers using while loop
#for loop
def printNnumbers(n):
    for i in range(1, n+1):
        print(i, end=' ')
    print("\n******* ")

#while loop 

def printNnumberwhile(n):
    i=1
    while i in range(1,n+1):
        print(i, end=' ')
        i+=1
    print("\n******* ")

#Write a Python code to print the following number pattern using a loop.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
def printPattern1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print (j, end=' ')
        print("\n")
    print("*****")


#Print multiplication table of a given number
def mult(n):
    for i in range(1,11):
        print (f"{n}x{i}={n*i}")


# Display numbers from a list using a loop
def print_list(numsList):
    for i in range(len(numsList)):
        print(numsList[i], end=" ")
    print("\n******* ")   


#Display numbers from a list using a loop
def print_list2(numsList):
    for num in numsList:
        print(num, end=" ")
    print("\n******* ")

#Count the total number of digits in a number

def numOfDigits(n):
    print(f"Num of digits in number :{n}") 
    count = 0
    if n == 0:
        print(" is 1")
        return
    while abs(n) > 0:
        count=1+count
        n//=10
    print(f" is {count}")

def numOfDigits_math(n):
    import math
    if n==0 :
        return 1
    return int(math.log10(abs(n)))+1

def numOfDigits_oneliner(n): #simplest : cast number to string and return lenght of string
    return len (str(abs(n)))

#***************** main ***********************
# printNnumberwhile(10)
# printNnumbers(20)
# printPattern1(5)
# mult(9)
# print_list2([12,12,14,15,16,1,7])
print (f"numOfDigits_oneliner : {numOfDigits_oneliner(10)}")
# Get Largest Number in List
# Write a Python program to get the largest number from a list.
import random
list1 =[]
for i in range(10):
    list1.append(random.randint(-100,100)) #random integer generation

print(list1)
#logical implementation
largest = list1[0]
for i in range(len(list1)) :
    if(list1[i] > largest):
        largest = list1[i] 
print(f"Largest number : {largest}")
# Get Smallest Number in List
# Write a Python program to get the smallest number from a list.

smallest = list1[0]
for i in range(len(list1)) :
    if(list1[i] < smallest):
        smallest = list1[i] 
print(f"smallest number : {smallest}")

##############ways to populate lists ##################

zeroeslist = [0]*10
print(f"zeroeslist : {zeroeslist}")

#alternative way
zeroeslist_alt = [0 for i in range(10)]
listint = list(range(10)) #0 to 9 
print(f"listint : {listint}")

listint = list(range(2,10, 3)) #start , end , step
print(f"listint : {listint}")

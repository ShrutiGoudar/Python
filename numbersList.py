""" # Get Largest Number in List
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
#####consider the same approach and its pitfall for nested lists
x = [[0]*3]*3
x[0][0] = 1 # expected o/p : x = [[1,0,0], [0,0,0], [0,0,0]] actually : x = [[1,0,0], [1,0,0], [1,0,0]]
'''
whats happening here ? 
# This creates 3 references to the SAME list object
x = [[0]*3 ]*3

# It's equivalent to:
inner_list = [0, 0, 0]
x = [inner_list, inner_list, inner_list]  # All point to same object!
'''
#correct way :
x = []
for i in range(3):
    x.append([0]*3)


#alternative way
zeroeslist_alt = [0 for i in range(10)]
listint = list(range(10)) #0 to 9 
print(f"listint : {listint}")

listint = list(range(2,10, 3)) #start , end , step
print(f"listint : {listint}")
 """

############## oneline code to do above ################
## read input from user
#listFromUser = list(map(int, input("Enter space seperated numbers for list entry : ").split()))
listFromUser =[-12, 32, 122, 0, -321, 4, 5,0, 23, 65, -16]
print(listFromUser)

print(f"Maximum value in the list is : {max(listFromUser)}")
print(f"Minimum value in the list is : {min(listFromUser)}")
print(f"Number of zeroes in the list is {listFromUser.count(0)}")
print(f"Number of negative numbers in the list is "
      f"{len([x for x in listFromUser if x<0])}")

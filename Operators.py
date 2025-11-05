'''
enumerate : built-in function that takes iterable object and returns an enumerate object ie pairs of (index, item)
            by default start index is 0, this can be changed.
zip :
'''
""" 
mylist = ['a', 'v', 'x', 't']
for index, item in enumerate(mylist, start=10):
    print(index)

 """
#list comprehension 
#see the code below
mystring = "hello"
mylist = []
for letter in mystring:
    mylist.append(letter)
mylist.extend(list("world"))  # note the usage append would add another list at the end of original list
print(mylist)

#Now see above implementation using list comprehension 
mylist = [x for x in mystring] + list("world")
print(mylist)

# Demonstrating why if-else in list comprehension is a BAD IDEA:

# BAD APPROACH: Using conditional expression (if-else before for)
# This includes unwanted None values in the list!
bad_approach = [x if x%2 == 0 else None for x in range(0,11)]
print("Bad approach (with None):", bad_approach)
# Output: [0, None, 2, None, 4, None, 6, None, 8, None, 10]

# Even if we try to filter out None later, it's inefficient:
filtered_bad = [x for x in bad_approach if x is not None]
print("Filtered bad approach:", filtered_bad)

# GOOD APPROACH: Using filtering (if after for) 
# This only includes values that meet the condition!
good_approach = [x for x in range(0,11) if x%2 == 0]
print("Good approach (clean):", good_approach)
# Output: [0, 2, 4, 6, 8, 10]

print(f"Bad approach length: {len(bad_approach)} (includes None values)")
print(f"Good approach length: {len(good_approach)} (only even numbers)")
#Python program to sum all the items in a list.

list1 = [1,2,3,4,5]
list2 = [1,1,1,1,1]

sum = list1+list2  #list concatination
print ("List concatination" , end = " ") #using space seperator instead of printing in new line )
print(sum)
sum.clear()

sum = [list1[i]+list2[i] for i in range(len(list1))]
print("Sum : " , end = " \t") #using space seperator instead of printing in new line 
print (sum)

##
#Write a Python program to multiply all the items in a list.
##
mult = 10 * sum     ##  list is mulitpled not the list elements
#print(mult)
#o/p:  
# [2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6,
#  2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 
#  2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

mult.clear()
mult = [sum[i]*10 for i in range(len(sum))]
print("Multiplication " , end = "\t") #using space seperator instead of printing in new line )
print(mult)
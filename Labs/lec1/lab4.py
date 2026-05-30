#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab4
# @version : 1.00  
# @brief   : lists methods
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################


# .append() : using when you want to append an element at end of list 
mylist = ["alaa", "mohamed","moatasem",12,14,24]
mylist.append("shreen") # append this string at the end of the list
print(mylist) # print list after appending

mylist.append(["ibrahim","mahmoud","shady"]) # append list at the end of the list
print(mylist) # print list after appending
print(mylist[6]) # print a specific element inside the list
print(mylist[7][0]) # print a specific element inside the list in the inter list
print("*****************")
# extend() : using when you want to extend list by list ترتيب مهم فيها
listone = [1,2,3,4]
listtwo = ["a","b","c"]
listone.extend(listtwo)
print(listone)
print("*****************")
listtwo.extend(listone)
print(listtwo)
print("*****************")
      
# remove() : used when you want to rwmove an element from the list
testlist = ["shady","alaa", "mohamed","moatasem",12,14,24]
testlist.remove("shady")
testlist.remove(14)
print(testlist)
print("*****************")

# sort() :  used when you want to sort the list  as Ascending order
testlisttwo = [12,14,24,3,2,1,0]
testlisttwo.sort()
print(testlisttwo)
print("*****************")

# sort(reverse=True) :  used when you want to sort the list as Descending order
testlisttwo.sort(reverse=True)
print(testlisttwo)
print("*****************")

# reverse() :  used when you want to reverse the items of the list
testlistthree = [12,14,24,3,2,1,0]
testlistthree.reverse()
print(testlistthree)
print("*****************")

# clear() :  used when you want to delete the list
testlistfour = [12,14,24,3,2,1,0]
testlistfour.clear()
print(testlistfour)
print("*****************")

# copy() : used when you want to copy list to another list
a = [1,2,3,4,4,4,4,5]
b = a.copy()
print(b)
# count() : used when you want to count an element in the list 
print(a.count(4))
# index() : used when you want to get the index of an element in the list 
print(a.index(5))
# insert(index "insert object before this index" , object) : used when you want to insert an element in a specific position
a.insert(7,100)
print(a)
# pop() : : used when you want to search about an index and return the element
print(a.pop(5))



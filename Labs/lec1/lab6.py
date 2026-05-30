#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab6
# @version : 1.00  
# @brief   : set methods
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# set items are enclosed in {}
# set are not ordered ,you donot able to use index to access item 
# set indexing and slicing can not be done 
# item in sets must be unique
# set has only immutable data type (numbers , string , tuple ) note that set did not carry list and dictionary 

mysetone ={"ahmed",1,2,"omr"}
print(mysetone)

# union () if you want to concat between set
myset2= {1,2,3,4}
myset3 ={5,6,7,8,9}
print(myset2.union(myset3))

# add () if you want to add an element at the end of the set
myset4 = {1,2,3,4}
myset4.add(6)
print(myset4)

# we use pop with set to  get randam element from set
myset5 = {1,2,3,4,5,"a"}
print(myset5.pop())

# we use ==> discared () to search about an element in a set to delete it and if not found no error
# but if u use remove() to search about an element in a set and if not found error
myset5.discard(6)
print(myset5)

print("=" * 40)
print("=" * 40)
# difference() to know the difference between sets
# difference_update() to know the difference between sets and update the first set by difference and remove the other element
# intersection() to know the intersection part(المشترك) between sets
# intersection_update() to know the difference between sets and update the first set by difference and remove the other element
# symmetric() to know the difference between sets in all
# symmetric_difference_update() to know the difference between sets and update the first set by difference in all and remove the other element

myset6 =  {1,2,3,4,5}
myset7 =  {1,2,"shady","mohamed"}
print(myset6.difference(myset7)) #  ( myset6 - myset7 ) ==> the same result
print("_" * 40)
myset8 =  {1,7,8,4,5}
myset9 =  {1,2,"osama","mohamed"}
myset8.difference_update(myset9) # 
print(myset8)

print("*" * 40)
print("*" * 40)

myset10 =  {1,2,3,4,5}
myset11 =  {1,2,"shady","mohamed"}
print(myset10.intersection(myset11)) #  ( myset6 & myset7 ) ==> the same result
print(myset10)
print("*" * 40)
print("*" * 40)

myset12 =  {1,2,3,4,5}
myset13 =  {1,2,"shady","mohamed"}
myset12.intersection_update(myset13)
print(myset12)


print("-" * 40)
print("-" * 40)

myset14 =  {1,2,3,4,5}
myset15 =  {1,2,"shady","mohamed"}

print(myset14.symmetric_difference(myset15)) #  ( myset6 ^ myset7 ) ==> the same result

print("-" * 40)
print("-" * 40)

myset16 =  {1,2,3,4,5}
myset17 =  {1,2,"shady","mohamed"}
myset16.symmetric_difference_update(myset17)
print(myset16)



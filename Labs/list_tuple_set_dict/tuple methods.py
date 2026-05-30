#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab5
# @version : 1.00  
# @brief   : tuple methods
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# tuple items are enclosed in parantheses
# you can remove the parantheses if you want
# tuples are ordered ,to use index to access item 
# tuples are immutable ==> you can't add or delete or edit
# tuples are is not unique 
# tuples able to carry different data types
# operators used in string and list available in tuples

# tuple syntax

mytupleone =("mohamed", "bedier","shady")
mytupletwo ="mohamed", "bedier","shady",2,3,41

print(mytupleone) # print whole tuple
print(mytupletwo) # print whole tuple

print(type(mytupleone)) # print =====> tuple
print(type(mytupletwo)) # print =====> tuple

# tuple indexing
print(mytupleone[0])
print(mytupletwo[-1])

# tuple assign values
mytuplethree = (1,2,3,4,5,6)


# tuple with one element using ====> comma ,
mytuplefour = ("ibrahim",)
mytuplefive = "mohamed",

print(mytuplefour) # print whole tuple
print(mytuplefive) # print whole tuple
print(type(mytuplefour)) # print =====> tuple
print(type(mytuplefive)) # print =====> tuple
print(len(mytuplefour)) # print =====> 1
print(len(mytuplefive)) # print =====> 1

# tuple concatenaation
mytuplesix = (1,2,3,4,5,6)
mytupleseven = (7,8,9,10)
mytupleeight= mytuplesix + mytupleseven
print(mytupleeight)

# tuple destruct
# if u have a tuple and wanted to seperate its element into variable
a = ("A","B","C")
x,y,z = a
print(x)
print(y)
print(z)
# if u have a tuple and wanted to ignored an element when you seperate its element into variable using _
a = ("A","B",4,"C")
x,y,_,z = a
print(x)
print(y)
print(z)

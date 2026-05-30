#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab3
# @version : 1.00  
# @brief   : list
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################


# list items are anclosed in square brackets 
# list is ordered ,to use index to access item 
# list is mutable ===> can add , delete and edit 
# list can carry different element from different datatype
# list items is not unique can doublicate items

# example 
mylist = ["one","two","one",1,100.5,True]
# repeated data is allow
print(mylist) # print whole list  
print(mylist[1]) # print ===> one   
print(mylist[-1]) # print ===> True   
print(mylist[-3]) # print ===> 1   

# with slicing ====> ordered
print(mylist[1:4]) # print ===> "two","one",1
print(mylist[:4]) # print ===> "one","two","one",1
print(mylist[1:]) # print ===> "two","one",1,100.5,True
print(mylist[::2]) # print ===> "one","one",100.5

# editting on the list =====> mutable
mylist[1] = 2
mylist[-1] = False
mylist[0:3] = ["A","B","C","D"]
print(mylist)
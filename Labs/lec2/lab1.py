#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab3  
# @version : 1.00  
# @brief   : Strings and Indexing of c/c in a string
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# to define a string between double qoute
mystrone = "this string between double qoute"
print(mystrone)
print("*******************************")

# to define a string between single qoute
mystrtwo = 'this string between single qoute'
print(mystrtwo)
print("*******************************")

# to define a letter between single qoute  inside a string between a double qoute
mystrthree = "My Name is mohamed Bedier 'mohamed' "
print(mystrthree)
print("*******************************")

# to define a letter between double qoute  inside a string between a single qoute
mystrfour = 'My Name is mohamed Bedier "mohamed" '
print(mystrfour)
print("*******************************")

#define a multiline string between three double qoute
mystrfive = """first line 
second line 
thrid line 
"""
print(mystrfive)
print("*******************************")

#define a multiline string between three single qoute
mystrsix = '''first line 
second line 
thrid line 
'''
print(mystrsix)
print("*******************************")

# Indexing (Access Single item in a string)
mystrseven = "I love python" # define a string in a variable 

print(mystrseven[0]) # get the index of 0 from the start ===> I
print(mystrseven[5]) # get the index of 5 from the start ===> e
print(mystrseven[7]) # get the index of 7 from the start ===> p

# if the index is signed that means from the end
print(mystrseven[-1]) # get the index of 1 from the end ===> n
print(mystrseven[-3]) # get the index of 3 from the end===> h

#slicing (Access multiple sequence items)
# syntax: [start : end ] end not included
# syntax: [start : end : step]

print(mystrseven[8 : 11]) # this will print yth
print(mystrseven[3 : 5]) # this will print ov
print(mystrseven[: 10]) # note that if start is not here will start from 0 , this will print i love pyt
print(mystrseven[5: ]) # note that if end is not here will print untill the end , this will print e python
print(mystrseven[ : ]) # this will print full string


print(mystrseven[0 : : 1]) # this will print full string
print(mystrseven[0 : : 2]) # this will print c/c then continue a c/c 
#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab1   
# @version : 1.00  
# @brief   : Learn how to use print , comment and variables
#                (single line and multi line)
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################



# I use the function to print a string
print("hello python")
print("i love python")
print("***********************************")
# to know type of variables we using type() func
print(type("hello mohamed")) # type is string
print(type(10)) # type is integer
print(type(12.5)) # type is float 
print(type(5 == 2)) # type is boolean 
print(type([1,23,3,5,8])) # type is list 
print(type((1,2,3,4))) # type is tuple    
print(type({"one" : 1 , "two" : 2})) # type is dictionary
print("***********************************")
#--------------------------------------
# syntax to define a variable :
#  variable name = value or string
#  or 
#  datatype : variable name = value or string
#--------------------------------------

myname = "mohamed bedier" # define a variable and make it to carry a string
print(type(myname));print(myname) # ask about type of the var and print the variable myname

print("***********************************")
myname = 3 # define a variable and make it to carry a number
print(type(myname));print(myname) # ask about type of the var and print it
print("***********************************")
deciVariable = [1,2,3] # define a variable and make it to carry a list
print(type(deciVariable));print(deciVariable) # ask about type of the var and print it
print("***********************************")
deciVariable = "string" # define a variable and make it to carry a string
print(type(deciVariable));print(deciVariable) # ask about type of the var and print it
print("***********************************")
### to know keywords in python using help("keywords") :
print(help("keywords"))

# to define a variable as global variable
global var 


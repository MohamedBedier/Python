##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab4  
# @version : 1.00  
# @brief   : Strings Methods
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# define a string in a variable 
mystrone = "I love python" 
# define another string in another variable 
mystrtwo = "       I love python       " 

# get the length of two strings by len(string_variable_name) 
print(len(mystrone))
print(len(mystrtwo))

# we use strip() function to remove spaces from the start and the end of the string
print(mystrtwo.strip()) 

# we use rstrip() function to remove spaces from the start of the string
print(mystrtwo.rstrip())

# we use lstrip() function to remove spaces from the end of the string
print(mystrtwo.lstrip())


mystrthree = "#####Python#####"
# strip or rstrip or lstrip can take an argument or more
print(mystrthree.strip("#"))
print(mystrthree.rstrip("#"))
print(mystrthree.lstrip("#"))

# rjust(width , fill chat) and ljust(width , fill chat)
# if u did not write fill char ====> python fill with space
# exe to understand 

myname = "MOhamed"
print(myname.rjust(15,"@"))
print(myname.ljust(15,"@"))

# note that if you want to cut from string using ====> strip | rstrip | lstrip 
# note that if you want to add characters for string using ====> rjust | ljust 

mystrfour = "I Love 2d Graphics and 3g Technology and python"
# if you want to convert the string into a title using title() function
print(mystrfour.title())
# if you want to convert the string into a capitalize using capitalizetle() function
print(mystrfour.capitalize())



var_one, var_two, var_three = "1", "20", "3"
print(var_one.zfill(3))
print(var_two.zfill(3))
print(var_three.zfill(3))

mystring = "aHmed"
print(mystring.lower()) # convert from any upper case to lower case
print(mystring.upper()) # convert from any lower case to upper case


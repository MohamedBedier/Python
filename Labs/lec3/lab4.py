#! /usr/bin/env python3

# ##############################################################
# ##############################################################
# #                                                         
# # @file    : Lec3_Lab4
# # @version : 1.00  
# # @brief   : Function 
# # @author  : MOHAMED BEDIER MOHAMED                                                                                                            
# #                                                                                                       
# ##############################################################
# ##############################################################


# [1] a Function is a reusable block of code, do a specfic task
# [2] a Function run when you call it 
# [3] a Function a accept element to deak with called [parameters]
# [4] a Function can do the task without returning data
# [5] a Function can return data after job is finished 
# [6] a Function create to prevent DRY [don't repeat your-self]
# [7] a Function accept elements when you call it called [arguments]
# [8] there's a built in function and user defined function
# [9] a Function is for all team and all apps

# this is the syntax of the function.
# [1] this function don't take anything and  don't return anything
def function_name():
    print("hello from python inside the function")
    
# calling the function  
function_name()

# functions and its parameters
# [2] this function takes an argument and  don't return anything
def say_hello(name):
    print(f"hello {name}")
    
# this function takes a name to say hello to the argument ===> mohamed    
say_hello("mohamed")

def additions(num1,num2):
    print(num1 + num2)

# call the function
additions(100,50)    

"""
    task : take from the user first name, middle name and the last name
    note that : if any space delete it capitalize
                maddle name take the first charater only 
                last name capitalize 
"""


# implement the function
def Take_first_Middle_Last_Name ():
    first_name = input("please enter the first name : ")
    middle_name = input("please enter the middle name : ")
    last_name = input("please enter the last name : ")
    
    print(f"hello {first_name.strip().capitalize()} {middle_name.capitalize():.1s} {last_name.strip().capitalize()}")
    
    
# call the function
Take_first_Middle_Last_Name()    
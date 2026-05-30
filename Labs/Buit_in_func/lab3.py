# ##############################################################
# ##############################################################
# #                                                         
# # @file    : Built_in_func/lab3.py
# # @version : 1.00  
# # @brief   : Built_in_func                                                             
# #                                                                                                       
# ##############################################################
# ##############################################################


####################################
# ---------------------------------#
# ---------built in function-------#
# ---------------------------------#
# abs() : to get the absolute value 
# pow : to get the power of number 
# min() : 
# max() : 
# slice() : 
# ---------------------------------#

# sum(iterable, start) : to get sum of arguments
x = [1,10,19,40]
print(sum(x)) # sum of the numbers in the list 
print(sum(x,40)) # sum of the numbers in the list and add 40 on it
print("====================================")

# round(number,# of point digits ) : rounded to the nearest integer
print(round(150.501))

# range(start, end, step) : sequence from start to stop by step
print(list(range(0)))
print(list(range(10)))
print(list(range(5,10)))
print(list(range(10,100,10)))
print(list(range(10,101,10)))

# print()  : 
print("hello bedier")
print("hello" , "bedier")
print("hello" , "bedier","ali","omer", sep=" || ")
print("hello" , "bedier","ali","omer", end="\t")
print("how are you?", end=" || ")
print("thanks we are all fine", end=" \n")
print("and you?", end=" \n")



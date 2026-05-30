# ##############################################################
# ##############################################################
# #                                                         
# # @file    : Built_in_func/lab1.py
# # @version : 1.00  
# # @brief   : Built_in_func                                                             
# #                                                                                                       
# ##############################################################
# ##############################################################


####################################
# ---------------------------------#
# ---------built in function-------#
# ---------------------------------#
# all() : check on elements
# any() : check on elements
# bin() : to print binary representation of a  num
# id()  : to get the address of the variable
# ---------------------------------#

x = [1,0,3,4]
if all(x):
    print("all elements are true")
else:
    print("one or more element is false")
    
print("====================================")

x = [[1,0,3,4]]
if any(x):
    print("at least one element is true")
else:
    print("there is no element true")

print(f"=" * 36)

print(bin(0xa))

print(f"=" * 36)



# ##############################################################
# ##############################################################
# #                                                         
# # @file    : Lec3_Lab6
# # @version : 1.00  
# # @brief   : Function ==> lambda 
# # @author  : MOHAMED BEDIER MOHAMED                                                                                                            
# #                                                                                                       
# ##############################################################
# ##############################################################


# [1] it has no name
# [2] you can call it inline without defining it 
# [3] you can use it in return data from another function
# [4] lambda used for simple function and def handle the large tasks
# [5] lambda type is a function
# [6] lambda is one single expression not block of code


def say_hello(name , age) : return f"hello {name} your age is : {age}"

# syntax of the lambda
hello = lambda name , age : f"hello {name} your age is : {age}"


print(say_hello('mohamed' , 26))
print(hello('mohamed' , 26))

# to know the name of the function
print(say_hello.__name__)
print(hello.__name__)


print(type(hello))
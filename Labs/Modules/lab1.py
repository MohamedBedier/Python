# to use anymodule 
# syntax : import  Module_name
# or s
# syntax : from Module_name import funcName1,funcName2

'''
import random
print(f"u use random module to generate random float num : {random.random()}")
#to show all functions inside this module
print(dir(random)) 

print("= " * 20)
'''



# import one or two function from module
from random import randint,random

print(f"print rand integer: {randint(100,900)}")
print(f"print rand integer: {randint(100,900)}")
print(f"u use random module to generate random float num : {random()}")

print("= " * 20)


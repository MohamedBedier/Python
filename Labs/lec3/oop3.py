# class food:
#     def __init__(self):
#         print("A New Food Has Been Added")
#     def eat(self):
#         print("Eating Food")
        
        
# class apple(food):
#     def __init__(self):
#         super().__init__()
#         print("A New Apple Has Been Added")
        
        
# class  Data :
#     __myvar = 10
#     var = 20 
#     def __init__(self):
#         print ("A New Data Has Been Added")
        
        
# data_one = Data()
# print(data_one.var)
# # print(data_one.__myvar) # this will raise an error because __myvar is a private variable and can not be accessed outside the class
# print(Data._Data__myvar) # this is the way to access the private variable __               

# class number:
#     def __init__(self, num):
#         print ("data class initialized")
#         self.num = num
        
#     # operator overloading    
#     def __add__(self, other):
#         print(f"add method called {self.num} + {other.num}")
#         return self.num + other.num
# class float:
#     def __init__(self, num):
#         print ("data class initialized")
#         self.num = num
        
# number_one = number(10)
# number_two = float(20.5) 
# result = number_one + number_two
# print(result)           
   
   
    
# ##############################################################
# ##############################################################
# #                                                         
# # @file    : Lec3_Lab3
# # @version : 1.00  
# # @brief   : loop === > while loop
# # @author  : MOHAMED BEDIER MOHAMED                                                                                                            
# #                                                                                                       
# ##############################################################
# ##############################################################

# # while condition is true , the code will run
# # while condition is false, the else code will run

# a = 0 # this is a counter to break the conditions

# while a < 15 :
#     print (f"mohamed {a}\n") # this code will print from a = 0 to a = 14
#     a +=1
# else:
#     print("loop is done\n") # when a = 15 while condition is false and the else code is run

# # another example 

# # create an empty list 
# myFavouriteWebs = []

# # define a counter to determine the length of list elments
# maxNumWebs = 5 

# while maxNumWebs > 0 :
#     # input the new website
#     web = input("Website Name Without https:// ")
    
#     # Add the new website to the list 
#     myFavouriteWebs.append(f"https://{web.strip().lower()}")
    
#     # decrease one number from allowed websites
#     maxNumWebs -=1 
    
#     # print the add message 
#     print(f"website added , {maxNumWebs} place left")
    
#     # print the list 
#     print(myFavouriteWebs)
    
# else : 
#     print("you can't add more because the list is full")
    
peoples = ["noor","mohamed","sayed","ali"]

skills = ["C","python","c++"]

for name in peoples : 
    print(f"{name} skills is : ")
    
    for skill in skills :
        print(f"- {skill} ")
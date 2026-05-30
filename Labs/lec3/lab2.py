##############################################################
##############################################################
#                                                         
# @file    : Lec3_Lab2
# @version : 1.00  
# @brief   : log in system
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

admins =["Ahmed","Mohamed","Osama","Sameh","Mahmoud","Noorhan","Manal","Rahma"]


name = input("please,enter your name : ").strip().capitalize()

if name in admins :
    print(f"Hello {name} welcome back")
    
    options =input("Are you want to Update or Delete your name ? :").strip().capitalize()
    if options == "Update" or options =="U" : 
        admins[admins.index(name)] = input("please enter the updated name : ").strip().capitalize()
        print("Name updated.")
        print(admins)
        
    elif options == "Delete" or options =="D" :
        admins.remove(name)
        print(admins)
    else :
        print("Wrong options.")
else : 
   status =input("you are not admin,You want to add your name Yes or No :") .strip().capitalize()
   if status == "Yes" or status =="Y" : 
       admins.append(name)
       print(admins)
   else :
       print("Not add your name and you are not an admin")   
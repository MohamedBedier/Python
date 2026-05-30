##############################################################
##############################################################
#                                                         
# @file    : Lec3_Lab8
# @version : 1.00  
# @brief   : BISECTION SEARCH ALGORITHM example on mahra tech
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# guess a number from 0 to 100 

print("please think of a number between 0 to 100 ")
high_num = 100
low_num = 0 
med_num = (high_num + low_num)//2

state = True

while state : 
    print("is your secret number is " + str(med_num))
    guess= input( "Enter 'c' to indicate is to Game over,Enter 'h' to indicate is to high,Enter 'l' to indicate to low  :" )
    if guess == 'c':
        print("Game over.Your secret number was :" + str(med_num))
        state = False
    elif guess == 'h':
       high_num = med_num
       med_num = (high_num + low_num)//2     
    elif guess == 'l':
       low_num = med_num
       med_num = (high_num + low_num)//2     
    else :
        print("sorry.i do not understand your input")

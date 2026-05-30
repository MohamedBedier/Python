##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab5  
# @version : 1.00  
# @brief   : Strings Methods 2
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################


# define a string in a variable 
mystrone = "I love python and c programming language" 

# we use split() function to convert the string into list seperated by default on space in the string
print(mystrone.split()) 
# we use this function to know type 
print(type(mystrone.split())) 

print("******************")
mystrTwo= "I-love-python-and-c-programming-language" 
# we use split() function to convert the string into list seperated by dash in the string
print(mystrTwo.split("-")) 

print("******************")
mystrthree= "I-love-python-and-c-programming-language" 
# we use split() function to convert the string into list seperated by dash in the string,but only for 2 dash from the left
print(mystrthree.split("-",2)) 

print("******************")
mystrfour= "I-love-python-and-c-programming-language" 
# we use rsplit() function to convert the string into list seperated by dash in the string,but only for 2 dash from the right 
print(mystrfour.rsplit("-",2)) 

print("******************")
mystrfive= "mohamed" 
# we use center() function to add special character at the start of the string and at the end of the string 
# you must give at least one argument to this function ===> number of character add to the string 
# by default python add spaces 
# you can specify the pecial character you need
# the integer number "the argument" ===> contain string character number 
print(mystrfive.center(17) )
print(mystrfive.center(17,"#") )

print("******************")
mystrsix= "I-love-python-and-c-programming-language ,bec python is very easy"
# we use coun() to count string in a string 
print(mystrsix.count("python") ) #===> 2

# we use coun() to count string in a string from start index to end index
print(mystrsix.count("python",0,30) ) #===> 1 python word
print(mystrsix.count("python",0,56) ) #===> 2 python word


print("******************")
mystrseven= "MoHaMeD BeDiER" 
mystreight= "PyThOn Is My LanGuaGe"
# we use swapcase to swap any lower character to upper character and swap from upper to lower
print(mystrseven.swapcase())
print(mystreight.swapcase())

# row string you can use row tring r before string qoutes to use the string as it written
# for exe: 

mystring = print(r"mohamed \n bedier \t mohamed \:")

# another  exe : 
# note that print comments bec of r
regex = r"""
^              # start of line
(?P<name>\w+)  # capture a word
\s*=\s*
(?P<value>.+)  # rest of line
$"""
print(regex)

# if you want to print name in variable in a string 
myname = "Mohamed Bedier"
welcomeMessage = f"welcome {myname} to python world!" #replace mohamed bedier by {myname}
print(welcomeMessage)

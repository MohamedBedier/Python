##############################################################
##############################################################
#                                                         
# @version : 1.00  
# @brief   : Strings Methods
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# define a string in a variable 
mystrone = "I love python" 
# define another string in another variable 
mystrtwo = "       I love python       " 

# get the length of two strings by len(string_variable_name) 
print(len(mystrone))
print(len(mystrtwo))

# we use strip() function to remove spaces from the start and the end of the string
print(mystrtwo.strip()) 

# we use rstrip() function to remove spaces from the start of the string
print(mystrtwo.rstrip())

# we use lstrip() function to remove spaces from the end of the string
print(mystrtwo.lstrip())


mystrthree = "#####Python#####"
# strip or rstrip or lstrip can take an argument or more
print(mystrthree.strip("#"))
print(mystrthree.rstrip("#"))
print(mystrthree.lstrip("#"))

# rjust(width , fill chat) and ljust(width , fill chat)
# if u did not write fill char ====> python fill with space
# exe to understand 

myname = "MOhamed"
print(myname.rjust(15,"@"))
print(myname.ljust(15,"@"))

# note that if you want to cut from string using ====> strip | rstrip | lstrip 
# note that if you want to add characters for string using ====> rjust | ljust 

mystrfour = "I Love 2d Graphics and 3g Technology and python"
# if you want to convert the string into a title using title() function
print(mystrfour.title())
# if you want to convert the string into a capitalize using capitalizetle() function
print(mystrfour.capitalize())



var_one, var_two, var_three = "1", "20", "3"
print(var_one.zfill(3))
print(var_two.zfill(3))
print(var_three.zfill(3))

mystring = "aHmed"
print(mystring.lower()) # convert from any upper case to lower case
print(mystring.upper()) # convert from any lower case to upper case

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


# what is the different between index and find 
# index (substring , start , end) if the substring is not found return error 
# find  (substring , start , end) if the substring is not found return -1
# note that if the substring is doublicated return  the first substring index
# example to understand

mystr = "i love python very much"

print(mystr.index("y")) # ====> 8
print(mystr.index("p",0,15)) # ====> 7
# print(mystr.index("p",0,5)) # ====> ValueError: substring not found


print(mystr.find("o")) # ====> 3
print(mystr.find("p",0,15)) # ====> 7
print(mystr.find("p",0,5)) # ===> -1

# if you want to split every line as an element in a list using ===> splitlines()

mystrtwo = """first line 
second line 
third line """
print(mystrtwo.splitlines())

mystrthree = "first line\nsecond line\nthird line"
print(mystrthree.splitlines())

# istitle()
# isspace()
# islower()
# isupper()
# isalpha()
# isalnum()
# startwith()
# endwith()
mystrfour = "I Love Python And 3G"
mystrfive = "i love python and 3g"
mystrsix =" "
mystrseven = ""
mystreight = "MOHAMED"
mystrnine = "abcdefgh"
mystrten = "abcdef123"
print(mystrfour.istitle())  # ===> TRUE 
print(mystrsix.isspace()) # ===> TRUE 
print(mystrseven.isspace()) # ===> false 
print(mystrfive.islower()) # ===> TRUE 
print(mystreight.isupper()) # ===> TRUE 
print(mystrnine.isalpha()) # ===>true
print(mystrten.isalpha()) # ===>false
print(mystrnine.isalnum()) # ===>true
print(mystrten.isalnum()) # ===>true
print("*********************")
print(mystrfour.startswith("I"))  # ===> TRUE 
print(mystrfour.endswith("3G"))  # ===> TRUE 
print("*********************")

# if u want to replace string by another string using ==> replace(old val , new , count)

str = "Hello one two three one one"
print (str.replace("one","1")) # the first old val and end
print (str.replace("one","1",1)) # the first old val and end 
print (str.replace("one","1",2)) # the first and second old val and end 
print (str.replace("one","1",3)) # the first , second ,and the third old val and end 

# if u want to join list to a string using join(iteration)
mylist = ["mohamed","shady","bedier"]
print("-".join(mylist))
print(" ".join(mylist))
print(",".join(mylist))
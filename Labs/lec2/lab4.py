##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab6
# @version : 1.00  
# @brief   : Strings Methods 2
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

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
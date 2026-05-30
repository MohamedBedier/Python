##############################################################
##############################################################
#                                                         
# @file    : Lec3_Lab1
# @version : 1.00  
# @brief   : Boolean 
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# true values 
print(bool("mohamed"))
print(bool(100))
print(bool(90.5))
print(bool(True))
print(bool([1,2,3]))
print(bool(("mohamed",100,10.5)))
print(bool({"name":"ibrahim"}))

print("*" * 30)
# false values 
print(bool(0))
print(bool(''))
print(bool(""))
print(bool(False))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))

print("*" * 30)

# calculate your age
age =int(input('what\'s your age ? ').strip())

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("you lived for : ")
print(f"{months} months \n{weeks:,} weeks\n{days:,} days\n{hours:,} hours\n{minutes:,} minutes\n{seconds:,} seconds")




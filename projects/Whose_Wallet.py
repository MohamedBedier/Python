#inclse random module
import  random
#message for the user
print("Welcome to 'whose wallet?'")
print("You will give me a list of names, and i will pick a person to pay")
#ask the user to enter names seperated by comma
Names_List = input("if you're ready, enter the names seperated by a comma: ")
#split the list
names = Names_List.split(", ")
#calculate the length of list
length_of_list = len(names)
#generate random number between 0 to length_of_list
final_name =random.randint(0,length_of_list)
#print who pay
print(f"please ask '{names[final_name]}' to take his wallet out. Dinner is on him")


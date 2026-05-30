#message for user
print("*** Welcome to the multipication table ***")
#ask the user to enter a number
Number = int(input("Enter a number: "))
#message for user
print(f"Multiplication table for {Number} : \n")
# looping for print multi table
for i in range(1,11):
    print(f"8 x {i} = {Number*i}")
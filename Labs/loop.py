import math
numbers = [1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    if(x % 2 == 0):
        print(f"{x}\n")

print("Finished the loop successfully")

Attendance = ["Mohamed" , "Ibrahim" , "Osama" , "Amr"]
for Person in Attendance :
    if Person in Attendance :
        print(Person)
        option = input("Is this person attending? (yes/no): ").lower()
        if option == "yes":
            print("Attendance Confirmed!")
        else:
            print("Attendance not Confirmed")
        print("___________")
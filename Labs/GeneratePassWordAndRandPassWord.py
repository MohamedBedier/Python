import random

PassWord_Num = int(input("Enter a 4-digit PIN code:"))
Number_Length = len(str(PassWord_Num))

rand_num_from_PC = random.randint(1000,9999)

if Number_Length == 4:
    if PassWord_Num == rand_num_from_PC:
        print("Congrates! PIN code matched")
    else:
        print("Failure! PIN code did not match.\n")
        print(f"The computer generated this PIN: {rand_num_from_PC}")

else:
    print("Please enter 4 digit only")
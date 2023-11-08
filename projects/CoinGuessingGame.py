#include import module
import  random

#messages to the user
print("Welcome to the Coin Guessing Game!\n")
print("Choose a method to toss the coin:\n")

# these are user's options
print("1. Using random.random()\n")
print("2. Using random.randint()\n")

# take user's option 1 or 2 , don't forget to convert into int
Option_Num=int(input("Enter your choice (1 or 2): "))
# check on Option_Num
if Option_Num == 1:
    # ask the computer to gussing a number float between 0 and 1
    Float_Generate_num=random.random()
    # check on this number Float_Generate_num
    if Float_Generate_num >=0.5 :
        PC_Coin_Guess = "heads"
    else :
        PC_Coin_Guess = "tails"

    # ask the user to gussing Heads or Tails
    User_Coin_Guess=input("Enter your Guess (Heads or Tails): ").lower()

    if User_Coin_Guess != PC_Coin_Guess:
        print("Sorry, you lost!")
    else:
        print("Congratulations! You won!\n")
        print(f"The computer's coin toss result was: {PC_Coin_Guess}")

elif Option_Num == 2:
    # ask the computer to gussing a number INT_Generate_num between 0 and 1
    INT_Generate_num = random.randint(0,1)

    # check on this number INT_Generate_num
    if INT_Generate_num == 0:
        PC_Coin_Guess = "heads"
    else:
        PC_Coin_Guess = "tails"
    # ask the user to gussing Heads or Tails
    User_Coin_Guess = input("Enter your Guess (Heads or Tails): ").lower()
    #check on User_Coin_Guess and save_PC_Coin_Option
    if User_Coin_Guess != PC_Coin_Guess :
        print("Sorry, you lost!")
    else:
        print("Congratulations! You won!\n")
        print(f"The computer's coin toss result was: {PC_Coin_Guess}")

else:
    print("Invalid choice Please select either 1 or 2")
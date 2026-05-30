#message for the user
print("Welcome to place the rabbit\n")


#print the initial shap of matrix
Init_Matrix = [["🍃","🍃","🍃"], ["🍃","🍃","🍃"], ["🍃","🍃","🍃"]]

print(f"{Init_Matrix[0]} \n{Init_Matrix[1]} \n{Init_Matrix[2]}")

#message for the user
print(f"Where should the rabbit go? [🐇]")
#ask and take the row and the column which the rabbit go in it
PositionOfRabbit = input("Please choose a row and a column : ")

#split of two numbers
Row = int(PositionOfRabbit[0])
Col = int(PositionOfRabbit[1])


Init_Matrix[Row-1][Col-1]= "🐇"
#message for the user
print("\nSuccess ....\n")

#print the final position of rabbit
print(f"{Init_Matrix[0]} \n{Init_Matrix[1]} \n{Init_Matrix[2]}")
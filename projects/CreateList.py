Colors_List=[]
Colors_List.append(input("Add the first color you like: "))
Color_choice=input("Do you want to add more colors? Yes or No? ").lower()
if Color_choice == "yes":
    Colors_List.append(input("Add another color to the list: "))
    print("the colors you like are:")
    print(Colors_List)
else:
    print("the colors you like are:")
    print(Colors_List)
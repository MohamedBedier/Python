#initiate the list
Initial_List = [["Apples","Bananas"],["Milk","Water"]]
#print list before any update
print(Initial_List)
# make updates on the list
Initial_List [0].insert(0,"Oranges")
Initial_List [0].append("Kiwis")
Initial_List [1].remove("Water")
Initial_List [1].insert(0,"Coffee")
Initial_List [1].append("Tea")
Initial_List.append([1,2,3])
#messages for the user
input("press enter to change the content  .....")
print("Here is the updated basket")
#print list after updates
print(Initial_List)
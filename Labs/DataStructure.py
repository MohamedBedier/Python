#create a list
MyFavorite_FriendsList = ["Amr","Osama","Mahmoud","Amer","El_awadi","Yousef"]
#print the first element on our list and the last element on our list
print(f"The first name on our list is {MyFavorite_FriendsList[0]} and the last name on our list is {MyFavorite_FriendsList[-1]}")
#print the all element on the list
print(MyFavorite_FriendsList)
# how to edit on the list
MyFavorite_FriendsList[1]="osamaSami"
print(MyFavorite_FriendsList)

#create an empty list
color=[]
color.append("red")
print(color)

#extend list
MyFavorite_color=["red","green","yellow"]
MyFavorite_color.extend(MyFavorite_FriendsList)
print(MyFavorite_color)

#remove
numbers=[1,2,3,4,5,56]
print(numbers)
numbers.remove(56)
print(numbers)
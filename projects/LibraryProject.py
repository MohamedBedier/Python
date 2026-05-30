#define a list for books already have it in my library
Book_list=[]

#define a list for books i wish to have it in my library
Wish_list=[]

#ask the user to enter a name of a book which have it
Book_list.append(input("Enter the name of a book you own: ").lower())
#ask the user to enter another name of a book which have it
Another_book_choice_or_Enter = input("Enter the name of another book you own (or press 'Enter' to skip): ").lower()
#check on Another_book_choice_or_Enter
if Another_book_choice_or_Enter:
    #the user already enter a name of a book
    Book_list.append(Another_book_choice_or_Enter)
    print(f"Your library: {Book_list}")

else:
    #in case the user press enter
    print(f"Your library: {Book_list}")

#ask the user to enter a name of a book which have it in the future
Wish_list.append(input("Enter the name of a book you wish to have in the future: ").lower())
#ask the user to enter another name of a book which have it in the future
Another_Future_book_choice_or_Enter = input("Enter the name of another book you own (or press 'Enter' to skip): ").lower()

#check on Another_Future_book_choice_or_Enter
if Another_Future_book_choice_or_Enter:
    # the user already enter a name of a book
    Wish_list.append(Another_Future_book_choice_or_Enter)
    print(f"Your Wish_list: {Wish_list}")
else:
    # in case the user press enter
    print(f"Your Wish_list: {Wish_list}")

#ask the user , if he has any book from WishList
Book_already_have_from_Wish_list= input("Enter the name of a book from your wish list that you've acquired (or press 'Enter' to skip):").lower()
#check on Book_already_have_from_Wish_list
if Book_already_have_from_Wish_list:
    #user enter a name of a book which have it from Wish list
    Book_list.append(Book_already_have_from_Wish_list)
    print(f"Update library: {Book_list}")
    Wish_list.remove(Book_already_have_from_Wish_list)
    print(f"Update Wish_list: {Wish_list}")
else:
    # in case the user press enter
    print(f"Your library: {Book_list}")
    print(f"Your Wish_list: {Wish_list}")

#ask the user , if he Donated any book from Book list
Donate_Book_from_Book_list= input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip):").lower()
#check on Donate_Book_from_Book_list
if Donate_Book_from_Book_list:
    Book_list.remove(Donate_Book_from_Book_list)
    print(f"final library after Donations: {Book_list}")
else:
    # in case the user press enter
    print(f"ok,You did not donate by any book: {Book_list}")
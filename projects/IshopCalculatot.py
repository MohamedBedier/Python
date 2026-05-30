#define a list to carry items in basket
ItemInBasket = []
#define a list to carry items price in basket
ItemPriceInBasket = []


#message for user
print("***** Welcome to iShop calculator *****")
#ask the user to enter items are there in your basket
NumOfItemInBasket = int(input("How many items are there in your basket today? "))
if NumOfItemInBasket > 0:
    print("Let's get to counting them .... ")
    #looping to count the items in basket and its the cost
    for item in range(1,NumOfItemInBasket+1):
         itemName = input(f"please tell me the name of the item number {item} : ").lower()
         ItemInBasket.append(itemName)
         print(f"What is the price of {itemName}")
         itemPrice = float(input("$"))
         ItemPriceInBasket.append(itemPrice)

    #ask user to enter if wants to see items into list or not
    userDecision = input("Would you like to see your entire basket items?(yes,no) ").lower()
    if userDecision == "yes":
         print(ItemInBasket)
         userCostDecision = input("Would you like to see how much it'll cost?(yes,no) ").lower()
         if userCostDecision == "yes":

              print("Buying these items will cost:\n")
              print(sum(ItemPriceInBasket))
         else:
              input("press enter to exit")
    else:
        input("press enter to exit")
else:
    print("seems like you're not in the mood for shopping today")
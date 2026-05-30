#ask the user to enter length and convert into float
float_length = float(input("Please enter type Length:\n"))
#ask the user to enter width and convert into float
float_widht = float(input("Please enter type Width:\n"))
#ask the user to enter price and convert into float
float_pric = float(input("how much for meter:\n"))
#calculate the area 
float_area = float_length * float_widht
#calculate the toral price
float_total = float_area * float_pric
#convert float_area into string 
str_area = str(float_area)
#convert float_total into string 
str_total = str(float_total)
#print the total area 
print("the total area is: " + str_area)
#print the total price 
print("Give the guy : " + "$" + str_total)

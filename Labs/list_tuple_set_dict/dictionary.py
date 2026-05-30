#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab7
# @version : 1.00  
# @brief   : Dictionary
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################


# Dict items are enclosed in curly braces {key : value}
# Dict items are contains key : value
# Dict key need to be immutable ==> (number , string m tuple )==> list is not allowed 
# Dict key need to be unique 
# Dict value can have any data types
# Dict is not ordered you access its element with key

# example 
user = {
    "name" : "mohamed",
    "age" : 23,
    "country" : "Egypt"
}

print(user) # print whole dictionary
print(user["name"]) #===> "mohamed"
print(user.keys()) # print all keys in the dictionary
print(user.values()) # print all values in the dictionary

# two dim dictionary

mydictionary ={
    "one" : {
        "name" : "mohamed",
        "age" : 23,
    "country" : "Egypt"
    },
    "two" : {
        "name" : "shady",
        "age" : 30,
    },
    "three" : {
        "name" : "bedier",
        "age" : 15,
        "country" : "USA"
    }
}

print(mydictionary) # print whole dictionary
print(mydictionary["one"]) # print key and value of element one 
print(mydictionary["one"]["name"]) # print mahamed
print(len(mydictionary)) # three elemet in the  dictionary
print(len(mydictionary["two"])) # 2 elemet in the nested dictionary

# you can create dictionary from variables 
dictvarone = {
        "name" : "mohamed",
        "age" : 23,
    "country" : "Egypt"
    }
dictvar2 = {
        "name" : "shady",
        "age" : 30
    }
dictvar3 = {
        "name" : "bedier",
        "age" : 15,
        "country" : "USA"
    }

allvariables = {"one":dictvarone,"two":dictvar2,"three":dictvar3}
print(allvariables)

# if you want to update the dictionary 
myupdatedictionary = {
        "name" : "shady",
        "age" : 30
    }
print(myupdatedictionary)
myupdatedictionary.update({"country":"egypt","education": " programming"}) #adding this element to dictionary
print(myupdatedictionary)

print("=" * 40)
# setdefault() 
# we use it if we want to search about a key and if it found print it and if not ===> print default which entered by the user
# note thate if note found it will add key and default value into our dictionary

dictionary1 = {
    "name" : "mohamed"
}

print(dictionary1)
print(dictionary1.setdefault("age", 36)) #it will add key and default value into our dictionary
print(dictionary1)

# fromkeys() : it will create dictionary from varibles which entered from the user

a = ('mohamed','shady','bedier')
b = 'x'

print(dict.fromkeys(a, b)) # a => as a key , b => as a value
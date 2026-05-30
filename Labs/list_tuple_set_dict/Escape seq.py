#!/usr/bin/env python3

##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab2   
# @version : 1.00  
# @brief   : Escape sequences characters
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################


##############################################################
# \b ===> Back space 
# \newline ===> escape new line + \ 
# \\ ===> escape back slash
# \' ===> escape single qoute 
# \" ===> escape double qoute 
# \n ===> escape new line
# \r ===> carriage return 
# \t ===> Horizential tab
##############################################################

# back space \b
print ("Hello\bworld!!") # Note that o c/c will be deleted 

print("***********************************")
# escape new line + \ 
print ("Hello\
 world!!") # Note that hello world will print in one line

print("***********************************")
# escape back slash \\
print ("Hello \\ world!!") # Note that ====> hello \ world 

print("***********************************")
# escape single qoute \'
print ("Hello \' world!!") # Note that ====> hello \' world 

print("***********************************")
# escape double qoute \""
print ("Hello \" world!!") # Note that ====> hello \" world 

print("***********************************")
# escape new line  or escape feed
print ("Hello \n world!!") # Note that hello in a line and world in a line

print("***********************************")
# carriage return 
print ("123456789\rmohamed") # Note that will replace character by number mohamed89

print("***********************************")
# Horizential tab
print ("123456789 \t mohamed ") 
##############################################################
##############################################################
#                                                         
# @file    : Lec1_Lab7
# @version : 1.00  
# @brief   : Strings formatting
# @author  : MOHAMED BEDIER MOHAMED                                                                                                            
#                                                                                                       
##############################################################
##############################################################

# place holder %

myname = "mohamed bedier"
myage = 26
myrank = 10

# if we need to concat. string  and num by using %
print("my name is : " + myname)
print("***************************")
print(f"my name is : {myname}")
print("***************************")
print("my name is : %s" % myname)
print("***************************")
print("my name is : %s and my age is : %d" %( myname,myage))
print("***************************")
print("my name is : %s and my age is : %d and my rank is : %0.2f" %( myname,myage,myrank))


# if we use .format()
print("***************************")
print("my name is : {}".format(myname))
print("***************************")
print("my name is : {} and my age is : {}".format( myname,myage))
print("***************************")
print("my name is : {} and my age is : {} and my rank is : {}".format( myname,myage,myrank))

# another way to use .format()
print("***************************")
print("my name is : {:s}".format(myname))
print("***************************")
print("my name is : {:s} and my age is : {:d}".format( myname,myage))
print("***************************")
print("my name is : {:s} and my age is : {:d} and my rank is : {:0.2f}".format( myname,myage,myrank))

# format money
mymoney = 500162859365

print("my money in bank is : {:,d}".format(mymoney))






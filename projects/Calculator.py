from math import  *

def SUM_Func(Num1,Num2) :
    return  Num1 + Num2

def SUb_Func(Num1,Num2) :
    return  Num1 - Num2


def Mult_Func(Num1, Num2):
    return Num1 * Num2
def Remend_Func(Num1,Num2) :
    return  Num1 % Num2

def Div_Func(Num1,Num2) :
    if Num2 != 0:
        return  Num1 / Num2
    else:
        print("You are trying to divide by 0")


Sum = SUM_Func(5,7)
print(f"sum = {Sum}")
Sub = SUb_Func(5,7)
print(f"sub = {Sub}")
Mult = Mult_Func(5,7)
print(f"Mult = {Mult}")
Remend = Remend_Func(8,2)
print(f"Remend = {Remend}")
Div = Div_Func(9,0)
print(f"Div = {Div}")
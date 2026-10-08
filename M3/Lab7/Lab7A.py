# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 7


def isValid(op1,op2):
    if op1+op2>30:
        return True
    else:
        return False

def area(op1,op2):
    return op1*op2

def perimeter(op1,op2):
    return 2*(op1+op2)


while True:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    valid = isValid(width,height)
    if valid == True:
        print("This is a valid rectangle.")
        area = area(width,height)
        per = perimeter(width,height)
        print("The area is:",area)
        print("The perimeter is:",per)
    else:
        print("This is an invalid rectangle.")

    cont = input("Do you want to enter another width and height (Y/N)?: ")
    if cont != "Y":
        print("Program Ends")
        break





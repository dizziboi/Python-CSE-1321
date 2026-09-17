# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
notDoable = 0
triType = ""
triSide1 = int(input("Enter the first side of the triangle: "))
if triSide1 == 0:
    notDoable = 1
triSide2 = int(input("Enter the second side of the triangle: "))
if triSide2 == 0:
    notDoable = 1
triSide3 = int(input("Enter the third side of the triangle: "))
if triSide3 == 0:
    notDoable = 1
S1S2T = triSide1 + triSide2

if notDoable == 1: #Sees if a triangle has 0 sides
    print("Invalid input. All sides must be greater than 0.")
else:
    if S1S2T <= triSide3: #Sees if there are more sides on side 1 or side 2 than side 3
        print("The sides do not form a valid triangle.")
    else:
        if triSide1 == triSide2 == triSide3:
            print("The triangle is an equilateral triangle.")
        elif triSide1 == triSide2:
            print("The triangle is an isosceles triangle.")
        elif triSide1 == triSide3:
            print("The triangle is an isosceles triangle.")
        elif triSide2 == triSide3:
            print("The triangle is an isosceles triangle.")
        else:
            print("The triangle is a scalene triangle.")




# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
triSide1 = int(input("Enter the first side of the triangle: "))
triSide2 = int(input("Enter the second side of the triangle: "))
triSide3 = int(input("Enter the third side of the triangle: "))
S1S2T = triSide1 + triSide2
S1S3T = triSide1 + triSide3
S2S3T = triSide2 + triSide3

if (triSide1 <= 0) or (triSide2 <= 0) or (triSide3 <= 0): #Checks if any of the sides are 0
    print("Invalid input. All sides must be greater than 0.")
elif (S1S2T <= triSide3) or (S1S3T <= triSide2) or (S2S3T <= triSide1): #Checks if one side has more sides than the others
    print("The sides do not form a valid triangle.")
elif triSide1 == triSide2 == triSide3: #Checks if all sides are the same
    print("The triangle is an equilateral triangle.")
elif triSide1 == triSide2:
    print("The triangle is an isosceles triangle.")
elif triSide1 == triSide3:
    print("The triangle is an isosceles triangle.")
elif triSide2 == triSide3:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")




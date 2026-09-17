# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1

print("Welcome!")
num = float(input("Please input a number: "))
print("")
print("What would you like to do with this number:")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")
numInput = int(input())

match numInput:
    case 0:
        if num == 0:
            print("Invalid option! ")
        else:
            print("\nThe additive inverse of", num, "is", num * -1)
    case 1:
        if num == 0:
            print("Cannot divide by 0! ")
        else:
            recip = 1 /num
            print("\nThe reciprocal of", num, "is", round(recip,3))
    case 2:
        numSquared = num*num
        print("\nThe Square of", num,"is", numSquared)
    case 3:
        numCubed = num*num*num
        print("\nThe cube of", num, "is", numCubed)
    case 4:
        print("\nThank you, goodbye! ")
    case _:
        print("\nInvalid option! ")
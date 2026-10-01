# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 6
Active = True
total = 0
def menu():
    print("\nMultiplication and Exponent Calculator")
    print("Choose option 1 for Multiplication")
    print("Choose option 2 for Exponentiation")
    print("Choose option 3 to Exit")

while Active:
    menu()
    numInput = int(input(""))
    match numInput:
        case 1:
            op1 = int(input("Enter an operand: "))
            op2 = int(input("Enter the other operand: "))
            for i in range(op2):
                total+=op1
            print(total)
        case 2:
            a = int(input("Enter the base: "))
            b = int(input("Enter the exponent: "))
            total = a
            for i in range(b-1):
                c = total
                total =0
                for j in range(c):
                    total+=a
            print(total)

        case 3:
            print("\nClosing the Calculator...")
            Active = False
        case _:
            print("\nInvalid Choice\n")

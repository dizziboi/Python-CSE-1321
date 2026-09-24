# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
num = int(input("Please enter a value for the size: "))
print("This is the requested "+ str(num) +"x"+ str(num), "box:")
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end="")
    print()
print("This is the requested right-facing "+ str(num) +"x"+ str(num), "triangle:")
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("This is the requested left-facing "+ str(num) +"x"+ str(num), "triangle:",end="")

for i in range(1,num+2):
    for j in range(num):
        if j >=(num+1-i):
            print("*",end="")
        else:
            print(" ", end="")
    print()
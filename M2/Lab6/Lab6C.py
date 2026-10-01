# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 6
NumRows = int(input("Enter Number for Rows or 0 to quit: "))
# while True:
#     if NumRows == 0:
#         break
#     else:
for i in range(1,NumRows+1):
    print(" "*(NumRows-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()


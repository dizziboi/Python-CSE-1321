# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1

num = int(input("Enter an odd number for the size of the diamond: "))
numCheck = num % 2
i = 0
counter = 0

if numCheck == 0:
    num = num+1
    print("Size must be an odd number; we will increase it to",num)

for i in range((num//2)+1):
    s=num//2-i
    num0=(i*2)+1
    print(" "*s,end="")
    for j in range(num0):
        print(counter%10,end="")
        counter=counter+1
    print(" ")

for k in range(num//2):
    s=k+1
    print(" "*s,end="")
    for l in range(num-2*s):
        print(counter%10,end="")
        counter=counter+1
    print(" ")

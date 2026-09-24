# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
cnt = 1
large = 0
print("Please enter 10 numbers and this program will display the largest.")
for cnt in range(cnt,11):
   num = int(input("please input number " + str(cnt) +": "))
   if num > large:
       large = num
print("\nThe largest number was " , large)


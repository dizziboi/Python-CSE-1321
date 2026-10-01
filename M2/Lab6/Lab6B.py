# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 6

import random
random_number = random.randint(1, 100)
#print(random_number)
print("Guess the number I am thinking!")
active = True
while active:
    NG = int(input("Enter any number between 1 and 100: "))
    if NG < random_number:
        print("To low!")
    elif NG > random_number:
        print("To high!")
    elif NG == random_number:
        print("Correct! I was thinking of",random_number)
        active = False
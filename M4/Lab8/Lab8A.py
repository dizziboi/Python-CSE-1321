# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 8

import random

seed = int(input("Enter a seed value: "))
rolls = int(input("How many times would you like to roll the die? "))
random.seed(seed)

total = 0

for i in range(1, rolls+1):
    roll = random.randint(1,6)
    print(f"Roll {i}: {roll}")
    total += roll

print(f"Total: {total}")
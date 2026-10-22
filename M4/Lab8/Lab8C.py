# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 8

import math

fn = float(input("Enter the first number"))
sn = int(input("Enter a second number"))

print(f"Celling: {math.ceil(fn)}")
print(f"Floor: {math.floor(fn)}")
print(f"Absolute value: {math.fabs(fn):.3f}")
print(f"Square root: {math.sqrt(sn):.3f}")
print(f"Cube root: {math.cbrt(sn):.3f}")
print(f"Math base 2: {math.log(sn,2):.3f}")
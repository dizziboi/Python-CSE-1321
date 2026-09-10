# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
grade = float(input("Enter your grade:"))
letterGrade= ""
if grade > 97:
    letterGrade = "A+"
elif grade >=97:
    print("A")
elif grade >=94:
    print("A-")
elif grade >=91:
    print("B+")
elif grade >=88:
    print("B")
elif grade >=85:
    print("B-")
elif grade >=82:
    print("C+")
elif grade >=79:
    print("C")
elif grade >=76:
    print("C-")
elif grade >=73:
    print("D+")
elif grade >=70:
    print("D")
elif grade >=67:
    print("D-")
else:
    print("F")
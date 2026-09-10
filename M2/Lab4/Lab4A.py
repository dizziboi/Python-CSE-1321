# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
grade = float(input("Enter your grade: "))
letterGrade= ""
if grade > 97:
    letterGrade = "A+"
elif grade >=97:
    letterGrade = "A"
elif grade >=94:
    letterGrade = "-A"
elif grade >=91:
    letterGrade = "B+"
elif grade >=88:
    letterGrade = "B"
elif grade >=85:
    letterGrade = "B-"
elif grade >=82:
    letterGrade = "C+"
elif grade >=79:
    letterGrade = "C"
elif grade >=76:
    letterGrade = "C-"
elif grade >=73:
    letterGrade = "D+"
elif grade >=70:
    letterGrade = "D"
elif grade >=67:
    letterGrade = "D-"
else:
    letterGrade = "F"

print("Letter grade is:",letterGrade)
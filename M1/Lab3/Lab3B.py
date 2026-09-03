# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
C1H = int(input("Course 1 hours: "))
C1G = int(input("Grade for course 1:"))
C2H = int(input("Course 2 hours: "))
C2G = int(input("Grade for course 2:"))
C3H = int(input("Course 3 hours: "))
C3G = int(input("Grade for course 3:"))
C4H = int(input("Course 4 hours: "))
C4G = int(input("Grade for course 4:"))
totalHours = C1H + C2H + C3H + C4H
totalQualityPoints = (C1H*C1G) + (C2G+C2H) + (C1H*C1G) + (C2G+C2H)
GPA = totalQualityPoints/totalHours

print(totalHours)
print(totalQualityPoints)
print(GPA)
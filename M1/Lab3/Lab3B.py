# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
C1H = int(input("Course 1 hours: "))
C1G = int(input("Grade for course 1:"))
qualityPoint1=C1H*C1G
C2H = int(input("Course 2 hours: "))
C2G = int(input("Grade for course 2:"))
qualityPoint2=(C2H*C2G)
C3H = int(input("Course 3 hours: "))
C3G = int(input("Grade for course 3:"))
qualityPoint3=(C3H*C3G)
C4H = int(input("Course 4 hours: "))
C4G = int(input("Grade for course 4:"))
qualityPoint4=(C4H*C4G)
totalHours = C1H + C2H + C3H + C4H
totalQualityPoints = qualityPoint1+qualityPoint2+qualityPoint3+qualityPoint4
GPA = totalQualityPoints/totalHours

print("Total hours:",totalHours)
print("Total quality points",totalQualityPoints)
print("Your GPA for this semester is ",round(GPA,2))
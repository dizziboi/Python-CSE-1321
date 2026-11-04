# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 10

def allMath(in1,in2):
    re1=in1+in2
    re2=in1-in2
    re3=in1*in2
    if in1 == 0 or in2 == 0:
        re4 = "None"
    else:
        re4=in1/in2
    if in1 == 0 or in2 == 0:
        re5 = "None"
    else:
        re5=in1//in2
    if in1 == 0 or in2 == 0:
        re6 = "None"
    else:
        re6=in1%in2
    re7=in1**in2
    return re1,re2,re3,re4,re5,re6,re7


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("Your resulting tuple is", allMath(num1,num2))
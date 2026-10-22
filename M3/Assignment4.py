# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 4

def input_choice(in1,in2):
    in1+=1
    in2+=2
    numIn = int(input("Choose an option: "))
    while in1 <= numIn >= in2:
        numIn = int(input("Type in a number"))
    else:
        return numIn

#def input_money

input_choice(1,4)
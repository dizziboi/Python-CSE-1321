# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
tempF = int(input("Enter temperature(F):"))
tempC = float((tempF-32)*5/9)
SOS = float(331+ 0.6 *tempC)

#print(tempC)
print("Sound travels at: ",SOS,"ms")
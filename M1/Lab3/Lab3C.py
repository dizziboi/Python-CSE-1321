# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
smallSandwich = int(input("Enter the number of small sandwiches:"))
ssTime = smallSandwich * 30
mediumSandwich = int(input("Enter the number of medium sandwiches:"))
msTime = mediumSandwich * 60
largeSandwich = int(input("Enter the number of large sandwiches:"))
lsTime = largeSandwich * 75
xlSandwich = int(input("Enter the number of extra-large sandwiches: "))
xlsTime = xlSandwich * 135

totalTime= ssTime+ msTime+ lsTime + xlsTime
minutes = int(totalTime/60)
seconds = totalTime %60

print("")
print("You've entered", smallSandwich, "small sandwiches.")
print("You've entered", mediumSandwich, "medium sandwiches.")
print("You've entered", largeSandwich, "large sandwiches.")
print("You've entered", xlSandwich, "extra-large sandwiches.")
print("")

print("Total cooking time is", minutes, "minutes and", seconds,"seconds.")
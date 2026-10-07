# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 3

print("[Character Frequencies]")
inStr=str(input("Enter a string: "))

inStr=inStr.lower()
inStr=inStr.replace(" ","")
while inStr:
    first=inStr[0]
    count = 0
    for ch in inStr:
       if ch== first:
           count+=1
    if count==1:
        print(first, "appears", count, "time")
    else:
        print(first,"appears",count,"times")
    inStr = inStr.replace(first, "")
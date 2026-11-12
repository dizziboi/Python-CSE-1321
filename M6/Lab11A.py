# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 11

class Chair:
    def __init__(self,numOfLegs=4,rolling=False,material="Wood"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material

#Asking for chair stuff
print("You are about to create a chair.")
numLegs = int(input("How many legs does your chair have: \n"))
roll = input("Is your chair rolling (true/false): \n")
if roll == "true":
    roll = True
elif roll == "false":
    roll = False
mat = input("What is your chair made of: \n")

#Creates user maid chair and default chair
userChair = Chair(numLegs,roll,mat)
defChair = Chair()

#determining if the chair can roll or not
if userChair.rolling:
    print("Your chair has",str(userChair.numOfLegs), "legs, is rolling, and is made of",str(userChair.material)+"." )
else:
    print("Your chair has",str(userChair.numOfLegs), "legs, is not rolling, and is made of",str(userChair.material)+"." )

print("This program is going to change that.")
print("Your chair has", str(defChair.numOfLegs), "legs, is not rolling, and is made of", str(defChair.material)+".")



numIn = input("Enter numbers (separate them with ,): ")
cnt = numIn.count(',')+1
print("You entered",cnt,"numbers.")
numIn=numIn.replace(",","") #get rid of commas in the input
CountE = 0
CountO = 0
CountZ = 0

for char in numIn: # Runs for how long the input is
    if int(char) % 2 == 0: #Checks if even
        CountE=CountE+1
    elif int(char) % 2 == 1: #Checks if odd
        CountO = CountO + 1
    if char == "0": ##Checks if the num is 0
        CountZ=CountZ+1

print("Even numbers:",CountE)
print("Odd numbers:",CountO)
print("Zeros:",CountZ)
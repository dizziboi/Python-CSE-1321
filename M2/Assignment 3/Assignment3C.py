# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 3

print("Welcome to the Guess the word game!")
inStr=str(input("Enter a word to guess (lowercase letters only): "))

guessed=""
while True:
    guess = ""
    for i in range(len(inStr)):
        if inStr[i] in guessed:
            guess=guess+" "+inStr[i]
        else:
            guess=guess+" _"
    print()
    print("The word to guess is:"+guess)
    letter=str(input("Guess a letter: "))
    guessed=guessed+letter
    if letter in inStr:
        print("Good guess!")
    else:
        print("Oops! That letter is not in the word.")
    missing=0
    for i in range(len(inStr)):
        if inStr[i] not in guessed:
            missing=missing+1
    if missing==0:
        print("Congratulations! You've guessed the word: " + inStr)
        break
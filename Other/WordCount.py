def CalcWord(sentence):
    count = 1
    for ch in sentence:
        if ch == " ":
            count = count + 1
    return count

while True:
    sen = input("Type in a sentence: ")
    count = CalcWord(sen)
    if sen == " " or sen == "":
        print("Invalid Input")
    else:
        print("There are", count, "words.")
    dec=input("Do you want to go again? (y/n): ")
    if dec == "n":
        break

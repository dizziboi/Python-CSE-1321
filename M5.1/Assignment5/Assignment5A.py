# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 5


def extract_letters(a):
    orgMessage = ""
    for char in a:
        if char.isdigit():
             continue
        else:
            orgMessage += char
    return orgMessage

def sum_digits(a):
    count = 0
    for char in a:
        if char.isdigit():
            count += int(char)
    return count

def rotate_word(a,b):
    neWord=[]
    for i in range (len(a)):
       neWord.append(a[(i+b)%len(a)])
    return "".join(neWord)

def decode_word(a):
    l=extract_letters(a)
    num=sum_digits(a)
    return rotate_word(l,num)

def main():
    MW=0
    WD=0
    dMess=[]
    message=input("Enter a secret message: ")
    messageList=(message.split(" "))
    for index in range(len(messageList)):
        decW=decode_word(messageList[index])
        if decW != messageList[index]:
            MW+=1
        if len(decW) != len(messageList[index]):
            WD+=1
        dMess.append(decW)
    print(f'Decoded message: {" ".join(dMess)}')
    print(f'Total words modified: {MW}')
    print(f'Words containing digits: {WD}')


main()

# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 5


enc_word = "py2th1on"

only_letters =""
for char in enc_word:
    if char.isalpha():
        only_letters = only_letters + char
    print(only_letters)

# sum = 0
# for char in enc_word:
#     if char.isdigit():
#         sum= sum +int(char)
# print(sum)

count = 0
for char in only_letters:
    print(char)
    only_letters = only_letters.removeprefix(char)
    print(only_letters)
    only_letters=only_letters+char
    print(only_letters)
    count = count +1
    if count == sum:
        break

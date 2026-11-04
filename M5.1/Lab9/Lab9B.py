# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 9
friends = []
print("[Friend List]\n")
while True:
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")
    option = int(input("Make your selection: "))

    if option == 1:
        name = input("\nEnter your friend's name: ")
        age = input("Enter your friend's age: ")
        print("Friend added")
        friend = (name,age)
        friends.append(friend)
        print()
    elif option == 2:
        print()
        for friend in friends:
            print(f"Name: {friend[0]}, Age: {friend[1]}")
        print()
    elif option == 3:
        print()
        print("Shutting down...")
        break

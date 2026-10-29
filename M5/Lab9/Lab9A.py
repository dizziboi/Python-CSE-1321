# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 9
print("[Mailing List]\n")
emails=[]
while True:
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")

    option = int(input("Make your selection: "))
    if option == 1:
        email= input("\nEnter the email to be added: ")
        emails.append(email)
        print("Email added to mailing list.\n")
    elif option == 2:
        email= input("\nEnter the email to be removed: ")
        if email in emails:
            print(f"{email} has been removed from the mailing list")
            emails.remove(email)
        else:
            print(f"No such email in mailing list: {email}")
        print()

    elif option == 3:
        print("Printing emails")
        print()
        for email in emails:
            print(email)
        print()
    elif option == 4:
        print()
        print("Shutting down...")
        break
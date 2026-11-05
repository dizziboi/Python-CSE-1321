# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 10

Users = {}
LoggedIn = False

while True:
    if LoggedIn:
        print("Choose an option")
        print("3 - Change Password")
        print("4 - Logout")
        print("E - Exit")
        ch = input()
    else:
        print("Choose an option")
        print("1 - Login")
        print("2 - Register")
        print("E - Exit")
        ch = input()

    match ch:
        case "1":
            print("\n[Login]")
            un = input("Username:")
            pw = input("\nPassword:")
            if un in Users and pw == Users[un]:
                print("\nSuccess!\n") #Change print statement
                LoggedIn = True
                LoggedInUser = un
            else:
                print("Incorrect username/password!\n")
        case "2":
            print("\n[Register]")
            un = input("Username:")
            pw = input("\nPassword:")
            Users[un]=pw
            #print(Users)
            print("\nUser successfully added!\n")

        case "3":
            print("\n[Changing password]")
            NewPw= input("Password: ")
            Users.update({LoggedInUser:NewPw})
            print()

        case "4":
            print("Logging Out...\n")
            LoggedIn = False
        case "E":
            print("\nTerminating...")
            break
        case _:
            print("Invalid input")
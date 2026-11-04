# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 10

Users = {}
LoggedIn = False
LoggedInUser = ""

while True:
    if LoggedIn:
        print("Choose an option")
        print("1 - Login")
        print("2 - Register")
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
            print("[Login]")
            un = input("Username: ")
            pw = input("Password: ")
            password = Users[un]
            if pw == password:
                print("You in nigga") #Change print statement
                LoggedIn = True
                LoggedInUser = un
            else:
                print("Incorrect username/password!")
        case "2":
            print("\n[Register]")
            un = input("Username: ")
            pw = input("Password: ")
            Users[un]=pw
            print("User successfully added!")
            print(Users,"\n") #Delete Later

        case "3":
            print("Changing something")
            print(LoggedInUser)

        case "4":
            print("Logging Out...")
            LoggedIn = False
        case "E":
            print("Goodbye")
            break
        case _:
            print("Invalid statement")
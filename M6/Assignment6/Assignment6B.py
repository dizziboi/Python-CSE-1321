# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 6

VendingMachine = {"A1":1.5,
                  "A2":2.5,
                  "B1":1.0,
                  "B2":2.5,
                  "C1":1.75
}

while True:
    print("========== VENDING MACHINE ==========")
    print("1)-Display Products")
    print("2)-Purchase Product")
    print("3)-Add New Product")
    print("4)-Sales Summary")
    print("5)-Exit")
    ch = input("Enter your choice: ")

    match ch:
        case "1":
            print("Available Products:")
            print("Code       Price")
            print("--------------------")
            for i in VendingMachine.items():
                print(i)
        case "1":
            print("Printting something")
        case "1":
            print("Printting something")
        case "1":
            print("Printting something")
        case "5":
            print("Thank you for using the vending machine!")
            break
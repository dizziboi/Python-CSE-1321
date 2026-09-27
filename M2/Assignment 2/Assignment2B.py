# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
Active = True
print("[Owl Airlines - Checked Bag Kiosk]")
while Active:
    status= input("Are you a Hooty Hoo Preferred Member? (Y/N): ")
    match status:
        case "Y":
            print("Welcome, and thank you for being a Hooty Hoo Preferred Member")
            print("As a perk for being awesome, your first 2 checked bags are free")
            print("Additional bags are $35.00 each\n")
            checking = input("Are you checking any bags? (Y/N): ")
            match checking:
                case "Y":
                    numCheck= int(input("How many bags are you checking in?: "))
                    if numCheck == 2:
                        print("As a Hooty Hoo Preferred Member your first 2 bags are complimentary.\n")
                        print("Have a safe flight and thank you for being a Hooty Hoo Preferred Member\n")

                    elif numCheck == 1:
                        print("As a Hooty Hoo Preferred Member all of your bags are complimentary.\n")
                        print("\nHave a safe flight and thank you for being a Hooty Hoo Preferred Member\n")
                    else:
                        numCheck = numCheck - 2
                        totalCost = numCheck * 35
                        print("As a Hooty Hoo Preferred Member your first 2 bags are complimentary.")
                        print("Checked Bag fees to pay: $"+str(totalCost))
                        print("\nHave a safe flight and thank you for being a Hooty Hoo Preferred Member\n")
                case "N":
                    print("\nHave a safe flight and thank you for being a Hooty Hoo Preferred Member\n")

        case "N":
            print("Checked Bag rates:")
            print("- First Checked bag: $35.00")
            print("- Second Checked bag: $50.00")
            print("- Third+ Checked bag: $150.00 each\n")
            checking = input("Are you checking any bags? (Y/N): ")
            match checking:
                case "Y":
                    numCheck= int(input("How many bags are you checking in?: "))
                    if numCheck == 1:
                        print("\nChecked Bag fees to pay: $35.00\n")
                    elif numCheck == 2:
                        print("Checked Bag fees to pay: $85.00")
                    elif numCheck >= 3:
                        totalCost = 85 +150*(numCheck-2)
                        print("\nChecked Bag fees to pay: $" + str(totalCost)+"\n")
                case "N":
                    print("")

print("[OwlMaps]")
print("Please enter the column letter and row number to figure out where you are in the Marietta Campus")
inCol = input("Enter the column letter (e.g., A-Y): ")
inRow = int(input("Enter the row number (e.g., 1 - 20): "))
findable = False
place = ""

if inCol == "K" and "L" and "M" and "N":
    findable = True
if inRow == 9 and 10 and 11 and 12:
    findable = True

if findable:
    if inCol == "K" and inRow == 9:
        place = "Science Lab Annex"
        print("You are in the " + place)

    if inCol == "K" and inCol == "L" and inRow == 10:
        place = "Engineering Lab Building"
        print("You are in the " + place)

    # elif (inCol == "K" or inCol == "L") and inRow == "11":
    #     place = "Design 2 Building"
    #     print("You are in the " + place)
    #
    # elif (inCol == "K" or inCol == "L") and inRow == "12":
    #     place = "K Field"
    #     print("You are in the " + place)
    #
    # elif inCol == "M" and inRow == "9" or inRow == "10":
    #     place = "Academic Building"
    #     print("You are in the " + place)
    #
    # elif inCol == "N" and inRow == "10" or inRow == "11" or inRow == "12":
    #     place = "Atrium Building"
    #     print("You are in the " + place)
else:
    print("We have trouble finding your location.")
# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 4

def input_choice(in1,in2):
    numIn = int(input("> "))
    while in1+1 <= numIn >= in2+1:
        print(f"Please, enter an option between {in1} and {in2}")
        numIn = int(input("> "))
    else:
        return numIn

def input_money():
    inMoney = int(input("> "))
    while inMoney < 0:
        print("Please, enter a valid monetary amount.")
        inMoney = int(input("> "))
    else:
        return inMoney

def burger():
    amount = 0.0
    while True:
        print()
        print("1. Big Owl Burger - Single ($5.99)")
        print("2. Big Owl Burger - Double ($7.99)")
        print("3. Return")
        choice = input_choice(1, 3)
        if choice == 1:
            print("1 Big Owl Burger - Single added")
            amount = amount + 5.99
        elif choice == 2:
            print("1 Big Owl Burger - Double added")
            amount = amount + 7.99
        elif choice == 3:
            break
    return amount

def sides():
    amount = 0.0
    while True:
        print()
        print("1. Fries ($3.49)")
        print("2. Onion Rings ($2.99)")
        print("3. Return")
        choice = input_choice(1, 3)
        if choice == 1:
            print("1 Fries added")
            amount = amount + 3.49
        elif choice == 2:
            print("1 Onion Rings added")
            amount = amount + 2.99
        elif choice == 3:
            break
    return amount

def drinks():
    amount = 0.0
    while True:
        print()
        print("1. Scrappy-Cola – Small ($2.49)")
        print("2. Scrappy-Cola – Medium ($2.79)")
        print("3. Scrappy-Cola – Large ($2.99)")
        print("4. Dr Owl – Small ($2.49)")
        print("5. Dr Owl – Medium ($2.79)")
        print("6. Dr Owl – Large ($2.99)")
        print("7. Return")
        choice = input_choice(1, 7)
        if choice == 1:
            print("1 Scappy-Cola - Small added")
            amount = amount + 2.49
        elif choice == 2:
            print("1 Scappy-Cola - Medium added")
            amount = amount + 2.79
        elif choice == 3:
            print("1 Scappy-Cola - Large added")
            amount = amount + 2.99
        elif choice == 4:
            print("1 Dr Owl - Small added")
            amount = amount + 2.49
        elif choice == 5:
            print("1 Dr Owl - Medium added")
            amount = amount + 2.79
        elif choice == 6:
            print("1 Dr Owl - Large added")
            amount = amount + 2.99
        elif choice == 7:
            break
    return amount

def calculate_tip(subtotal):
   #Calculates tip amount and formatting
    x = subtotal*.12
    x = round(x,2)
    y = subtotal*.2
    y = round(y,2)
    z = subtotal*.12
    z = round(z,2)
    print()
    print("Choose a tip option: ")
    print("1. $"+str(x),"(18%)")
    print("2. $"+str(y),"(20%)")
    print("3. $"+str(z),"(25%)")
    print("4. Custom")
    print("5. No tip")

    choice = input_choice(1,5)
    if choice == 1:
        return x
    elif choice == 2:
        return y
    elif choice == 3:
        return z
    elif choice == 4:
        print("Custom tip")
        custom = input_money()
        return custom
    elif choice == 5:
        return 0.0

def calculate_tax(subtotal):
    tax2 = subtotal *.06
    tax2 = round(tax2,2)
    return tax2

def print_total(subtotal,tip,tax):
    total = subtotal + tip + tax
    total = round(total,2)
    print()
    print("Subtotal: $"+str(subtotal))
    print("Tip: $"+str(tip))
    print("Tax: $"+str(tax))
    print("Total: $"+str(total))

def order():
    subtotal = 0.0
    while True:
        print()
        print("Choose an option: ")
        print("1. Burgers")
        print("2. Sides")
        print("3. Drinks")
        print("4. Check out")
        choice = input_choice(1, 4)
        if choice == 1:
            subtotal = subtotal + burger()
        if choice == 2:
            subtotal=subtotal+sides()
        if choice == 3:
            subtotal=subtotal+drinks()
        if choice == 4:
            tip = calculate_tip(subtotal)
            tax = calculate_tax(subtotal)
            print_total(subtotal,tip,tax)
            break
order()

#Debug code
#input_choice(1,4)
# tax = calculate_tax(2.99)
# print(tax)
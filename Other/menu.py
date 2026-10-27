def options():
    print("Enter 1 to print 'Hi'.")
    print("Enter 2 to print 'Hello'.")
    print("Enter 3 to print 'Namaste'.")
    print("Enter 4 to print 'Bonjour'.")
    print("Enter 5 to print 'Hola'.")

while True:
    options()
    option = int(input())
    if option == 1:
        print("Hi")
    elif option == 2:
        print("Hello")
    elif option == 3:
        print("Namaste")
    elif option == 4:
        print("Bonjour")
    elif option == 5:
        print("Hola")

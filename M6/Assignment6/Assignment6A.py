# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 6

class DeliveryRobot:
    def __init__(self,name,batteryL=100,dest=None):
        self.name = name
        self.bl = batteryL
        self.dest = dest
        self.deliveries = 0

    def assign_destination(self,newDest): #Sets the robots destination
        self.dest = newDest

    def has_destination(self):
        if self.dest is None:
            return False
        else:
            return True

    def deliver_package(self):
        if self.has_destination() and self.bl >= 25:
            self.bl =-25 #Takes 25% off of battery life
            self.deliveries =+1 #adds one to deliveries
            self.dest = None
            return True
        else:
            return False

    def recharge(self, amount):
        self.bl =+amount
        if self.bl >=100:
            self.bl = 100 #Makes sure the battery does not overcharge

    def get_robot_info(self):
        if self.has_destination():
            print(f"Robot: {self.name}")
            print(f"Battery: {self.bl}")
            print(f"Destination: {self.dest}")
            print(f"Completed Deliveries: {self.deliveries}")
        else:
            print(f"Robot: {self.name}")
            print(f"Battery: {self.bl}%")
            print(f"Destination: None")
            print(f"Completed Deliveries: {self.deliveries}")

class Robots:
    list_of_robots = []

while True:
    print("1 - Add a new robot")
    print("2 - Assign or change a destination")
    print("3 - Deliver a package")
    print("4 - Recharge a robot")
    print("5 - Display robots with assigned destinations")
    print("6 - Display all robots")
    print("7 - Exit")
    ch = input("> ")

    match ch:
        case "1":
            print("")
            inName = input("Enter robot name: ")
            battChoice = input("Use custom battery level? (y/n): ")
            if battChoice == "y":
                battP = int(input("Enter battery level: "))
            else:
                battP = None

            destChoice = input("Assign a destination? (y/n): ")
            if destChoice == "y":
               setDest = input("Enter destination: ")
            else:
                setDest = None

            print("Robot added successfully!\n")
            NewBot = DeliveryRobot(inName)
            Robots.append(NewBot)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("[Terminating program...]")
            break
        case _:
                print(Robots)
                print()



# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 6

robots_list = []

class DeliveryRobot:
    def __init__(self,name,bl=100,dest=None):
        self.name = name
        self.bl = bl
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
            print()


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
                battP = 100

            destChoice = input("Assign a destination? (y/n): ")
            if destChoice == "y":
               setDest = input("Enter destination: ")
            else:
                setDest = None

            print("Robot added successfully!\n")
            NewBot = DeliveryRobot(inName,battP,setDest)
            robots_list.append(NewBot)

        case "2":
            print("Choose a robot to assign a destination:")
            for index,robot in enumerate(robots_list):
                print(f"{index} {robot.name}")
            print()
            robot_index = int(input("> "))
            newDest = input("Enter destination: ")
            robots_list[robot_index].assign_destination(newDest)

        case "3":
            print("Choose a robot to deliver a package: ")
            for index, robots_list in enumerate(robots_list):
                if robot.has_destination():
                    print(f"[{index} {robot.name}")

            robot_index = int(input("> "))
            if robots_list[robot_index].deliver_package():
                print("Delivery completed")
            else:
                print("Delivery failed! Insufficient battery.")

        case "4":
            for index,robot in enumerate(robots_list):
                print(f"{index} {robot.name}")
            robot_index = int(input("> "))
            rechargeAmount= int(input("Enter recharge amount: "))
            robots_list[robot_index].recharge(rechargeAmount)

        case "5":
            print("\nRobots with assigned destinations: ")

            for index,robot in enumerate(robots_list):
                if robot.has_destination():
                    robots_list[index].get_robot_info()
            print()

        case "6":
            for index, robot in enumerate(robots_list):
                    robots_list[index].get_robot_info()

        case "7":
            print("[Terminating program...]")
            break
        #
        # #Debug code
        # case "q":
        #         print(robots_list)
        # case "d":
        #     for index, robots_list in enumerate(robots_list):
        #         print(f"{index} {robots_list.name} {robots_list.bl} ")
        #     print()
        #

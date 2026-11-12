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
            self.bl = 100 #Makes sure the battery does not over charge

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

Robots = []

while True:
    print("1 - Add a new robot")
    print("2 - Assign or change a destination")
    print("3 - Deliver a package")
    print("4 - Recharge a robot")
    print("5 - Display robots with assigned destinations")
    print("6 - Display all robots")
    print("7 - Exit")


#Debug
clanker = DeliveryRobot("Clanker1")
clanker.assign_destination("Georgia Tech")
print(clanker.has_destination())
clanker.get_robot_info()
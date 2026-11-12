# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 11

class Dog:
    def __init__(self,age,weight,name,furColor,breed):
        self.age = age
        self.weight= weight
        self.name=name
        self.furColor = furColor
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def rename(self,newName):
        self.name = newName

    def eat(self,food):
        self.weight+=food

print("You are about to create a dog.")
inAge = int(input("How old is the dog: \n"))
inWeight = float(input("How much does the dog weigh: \n"))
inName = input("What is the dog’s name: \n")
inColor = input("What color is the dog: \n")
inBreed = input("What breed is the dog: \n")

#Makes a new dog
cujo = Dog(inAge,inWeight,inName,inColor,inBreed)

print(str(cujo.name), "is a",str(cujo.age),"year old "+str(cujo.furColor),str(cujo.breed)+" that weighs "+ str(cujo.weight)+" lbs.")
cujo.bark()
eating = float(input(str(cujo.name)+ " is hungry, how much should he eat: \n"))
cujo.eat(eating)
newName = input(str(cujo.name)+ " isn’t a very good name. What should they be renamed to: \n")
cujo.rename(newName)
print(str(cujo.name), "is a",str(cujo.age),"year old "+str(cujo.furColor),str(cujo.breed)+" that weighs "+ str(cujo.weight)+" lbs.")

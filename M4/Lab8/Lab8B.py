# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 8

import time

timestamp = int(input("Type in a big whole number: "))
print(f"timestamp : {timestamp}")
print(f"Date and time: {time.ctime(timestamp)}")

pause = int(input("How much to wait"))
print("waiting")
time.sleep(pause)
print("Done")
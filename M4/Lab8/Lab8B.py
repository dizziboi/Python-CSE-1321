# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 8

import time

timestamp = int(input("Enter the timestamp in seconds: "))
print(f"Timestamp: {timestamp}")
print(f"Date and time: {time.ctime(timestamp)}")

pause = int(input("Enter pause length in seconds: "))
print("Waiting...")
time.sleep(pause)
print("Done!")
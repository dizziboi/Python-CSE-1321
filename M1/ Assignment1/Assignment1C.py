# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1
sampleRate = int(input("Enter Sample Rate (in Hz): "))
bufferSize = int(input("Enter Buffer Size: "))
trackLength = int(input("Enter track length (in seconds): "))

step1 = sampleRate*trackLength #Multiples the sample rate by the track length
step2 = step1 // bufferSize #Uses floor to find the full buffer
#print(step2)
step3 = step1 % bufferSize #Uses mod to find the leftover samples
#print(step3)
print("Processed",step2,"full buffers with",step3,"leftover samples.")

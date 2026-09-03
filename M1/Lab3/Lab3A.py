# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb
# Lab: 1
cc_Amount = float(input("Amount owed:$"))
APR = float(input("APR:"))
MPR = APR/12
MPR_P = MPR/100
min_Pay= cc_Amount * MPR_P



print("Monthly percentage rate:" ,round(MPR,3))
print("Minimum payment:$" ,round(min_Pay,2))
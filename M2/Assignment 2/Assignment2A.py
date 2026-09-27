# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Lab: 1


loud=(float(input("Enter input loudness (dB): ")))
TH=(float(input("Enter threshold (dB): ")))
print("Enter threshold (dB): ")
print("Select a ratio: ")
print("1 - 3:1")
print("2 - 4:1")
print("3 - 10:1")
SelRatio=int(input("> "))
if SelRatio==1:
    ratio=3
    print("")
elif SelRatio==2:
    ratio=4
    print("")
elif SelRatio==3:
    ratio=10
    print("")
else:
    ratio=2
    print("")
OutLevel=(((TH-loud)/ratio)-TH)*1
if loud<TH:
    print("Output Level:",loud,"dB")
else:
    print("Output Level:",OutLevel,"dB")

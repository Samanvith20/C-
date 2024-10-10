enterDistance=int(input("Enter distance: "))

if enterDistance <3:
    print("walk")
elif enterDistance<=15:
    print("Bike")
else:
    print("Car")
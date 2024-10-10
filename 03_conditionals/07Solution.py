EnterYourCoffeeSize = input("Enter your coffee size: ")
ExtraShot = input("Do you want an extra shot: ")


coffee = ""

if EnterYourCoffeeSize == "Tall" or EnterYourCoffeeSize == "Small" or EnterYourCoffeeSize == "Medium":
    coffee = EnterYourCoffeeSize + " coffee"
    if ExtraShot == "Yes":
        coffee += " with an extra shot"
else:
    print("Invalid coffee size")

if coffee:  
    print(coffee)

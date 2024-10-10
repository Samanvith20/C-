enterYourFavoriteFruit=input("Enter your favorite fruit: ")
print(enterYourFavoriteFruit)
enterYourColor=input("Enter your favorite enterYourColor: ")
print(enterYourColor)

if enterYourFavoriteFruit == "Banana":
    if enterYourColor == "Green":
        print("Unripe")
    elif enterYourColor == "Yellow":
        print("Ripe")
    elif enterYourColor == "Brown":
        print("OverRipe")
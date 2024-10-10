enterYourPetSpecies = input("Enter your pet species: ")
enterAge = int(input("Enter your age: "))
food=""
if enterYourPetSpecies == "Dog" and enterAge < 2:
    food="Puppy food"
elif enterYourPetSpecies == "Cat" and enterAge > 5:
    food="Senior cat food"
else:
    print("Invalid input")
if food:
    print(food)
    
userInputAge = int(input("Enter an age: "))
print(userInputAge)

day = input("Enter a day: ").lower()  
print(day)

# Determine base price based on age
if userInputAge >= 18:
    price = 12
else:
    price = 8

# Apply discount if it's Wednesday
if day == "wednesday":
    price -= 2

print("Ticket price for you is $", price)

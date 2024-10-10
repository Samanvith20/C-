userInputAge = int(input("Enter an age: "))
print(userInputAge)

if userInputAge < 13:
    print("Child")
elif userInputAge < 20:
    print("Teenager")
elif userInputAge < 60:
    print("Adult")
else:
    print("Senior")

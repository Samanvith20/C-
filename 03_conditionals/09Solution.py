enterYourYear = int(input("Enter your year: "))

if (enterYourYear % 4 == 0 and (enterYourYear % 100 != 0 or enterYourYear % 400 == 0)):
    print("Leap year")
else:
    print("Not a leap year")

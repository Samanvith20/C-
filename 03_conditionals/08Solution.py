EnterYourPassword=input("Enter your password: ")

if len(EnterYourPassword) < 6:
    print("Weak password")
elif len(EnterYourPassword) <= 10:
    print("Medium password")
elif len(EnterYourPassword) > 10:
        print("Strong password")
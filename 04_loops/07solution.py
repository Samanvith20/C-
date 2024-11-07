while True:
    try:
        enterAge = int(input("Enter a number between 1 and 10: "))
        if 1 <= enterAge <= 10:
            print("Thank you! You've entered a valid number.")
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

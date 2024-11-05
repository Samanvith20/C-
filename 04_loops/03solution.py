EnterNumber = int(input("Enter a number: "))  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

for i in numbers:
    if(i==5): continue
    result = EnterNumber * i                 # Multiply each number by EnterNumber
    print(f"{EnterNumber} * {i} = {result}")  # Print each result in a readable format

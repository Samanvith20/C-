# Get input from the user
n = int(input("Enter a number: "))

# Initialize the sum
sum_even = 0

# Loop through numbers up to n
for i in range(2, n + 1, 2):  #  check even numbers
    sum_even += i

# Output the result
print("Sum of even numbers up to", n, "is:", sum_even)

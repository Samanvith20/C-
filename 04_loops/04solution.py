my_str = "python"
reversed_str = my_str[::-1]  # Reverse the string using slicing
print(reversed_str)

 
 # Reverse the string using for loop
input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str  

print(reversed_str)
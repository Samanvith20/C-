# while **kwargs allows you to pass a variable number of keyword arguments as a dictionary. This provides flexibility in how functions can accept arguments.
# kwargs.items() returns a list of dictionary items, which can be used to iterate over the dictionary.

def print_all(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
print_all(name="John", age=25, city="New York")
print_all(name="Jane", age=22, city="San Francisco", country="USA")
print_all(name="Marie", age=30, city="Paris", country="France")
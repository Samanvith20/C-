class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

# Create an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", 100)

# Check if my_tesla is an instance of ElectricCar
print(isinstance(my_tesla, ElectricCar))  # Output: True

# Check if my_tesla is also an instance of Car (parent class)
print(isinstance(my_tesla, Car))  # Output: True

# Check if my_tesla is an instance of an unrelated class (e.g., int)
print(isinstance(my_tesla, int))  # Output: False

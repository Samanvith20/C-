class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery size: {self.battery_size} kWh"


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def engine_info(self):
        return f"Engine type: {self.engine_type}"


class ElectricCar(Battery, Engine):
    def __init__(self, brand, model, battery_size, engine_type):
        # Initialize parent classes
        Battery.__init__(self, battery_size)
        Engine.__init__(self, engine_type)
        self.brand = brand
        self.model = model

    def car_info(self):
        return f"{self.brand} {self.model}"


# Create an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", 100, "Electric")

# Access methods and attributes from both parent classes and ElectricCar
print(my_tesla.car_info())        # ElectricCar method
print(my_tesla.battery_info())    # Battery class method
print(my_tesla.engine_info())     # Engine class method

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
 
my_Ecar = ElectricCar('Audi', 'Q7', 100)
print(my_Ecar.brand)
print(my_Ecar.model)
print(my_Ecar.battery_size)               
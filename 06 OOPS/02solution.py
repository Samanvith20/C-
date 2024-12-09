class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    # Define fullName as a method of the class
    def fullName(self):
        return f"{self.brand} {self.model}"

my_car = Car('Audi', 'Q7')
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())

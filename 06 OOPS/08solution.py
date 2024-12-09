class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    @property
    def model(self):
        return self.__model
    
my_car = Car('Audi', 'Q7')
my_car.__model = 'Q8'
print(my_car.model)    # Access via @property, behaves like an attribute
    
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    @staticmethod
    def general():
         return "This is a general car"
 
 
my_car = Car('Audi', 'Q7')
print(my_car.general())
print(Car.general())    
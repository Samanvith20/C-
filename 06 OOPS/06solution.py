class Car:
    count = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.count += 1
        
my_car = Car('Audi', 'Q7')
my_car2 = Car('Audi', 'Q7')
print(Car.count)       
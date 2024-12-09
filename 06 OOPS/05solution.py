class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def fuel_type(self):
        return "Petrol"
  
class CarElectric(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        
    def fuel_type(self):
        return "Electric"   

my_car = Car('Audi', 'Q7')
my_Ecar = CarElectric('Audi', 'Q7')
print(my_car.fuel_type())
print(my_Ecar.fuel_type())      

# Polymorphism defines the same interface for different types of objects 
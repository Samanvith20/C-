class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
 
my_car = Car('Ford', 'Figo')
my_car.__brand = 'Audi'    # This will not change the value of __brand
# print(my_car.__brand)    # This will throw an error as __brand is a private variable
print(my_car.get_brand())
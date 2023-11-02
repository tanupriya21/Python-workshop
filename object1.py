class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

#Creating an object from the class
car1= Car("Toyota", "Camry")
car2= Car("Honda", "Civic")

print(car1.make, car1.model)
print(car2.make, car2.model)
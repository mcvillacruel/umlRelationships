# Inheritance
class Vehicle:
    pass

class Car(Vehicle):
    pass

# (Test)
my_car = Car()
print(isinstance(my_car, Vehicle))

# Object = A bundle of related attributes(variables) and methods(functions)
# You need a class to create many objects

# Class = (blueprint) used to design the structure and the layout of an object
from Car import Car

car1 = Car("Mercedes", 2025, "Black", True)
car2 = Car("Jeep", 2020, "Red", False)

print(car1)  # It will give me the code of the object 0x0000029BD7DF86E0
print("-------- Car 1--------")
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.sale)
print("----------------------")
print()
print("-------- Car 2--------")
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.sale)
print("----------------------")
car1.drive()
car1.stop()
car2.drive()
car2.stop()
print("----------------------")
print("-------- Car 1--------")
car1.carInfo()
print("----------------------")
print()
print("-------- Car 2--------")
car2.carInfo()
print("----------------------")

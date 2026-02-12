# Allows a class to inherit attributes and methods from another class
#                 Helps with code reusability and extensibility
#                 class Child(Parent)


print("#################### Inheritance #####################")
class Animals:
    def __init__(self, animalName):
        self.name = animalName
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Dog(Animals):
    def speek(self):
        print(f"{self.name} is WOOFING!")
class Cat(Animals):
    def speek(self):
        print(f"{self.name} is MEOWING!")
class Mouse(Animals):
    def speek(self):
        print(f"{self.name} is SQUEEKING!")
        
print("-------- Animal 1--------")
dog = Dog("Rocky")
print(dog.name)
dog.sleep()
dog.eat()
dog.speek()
print("----------------------")
print()
print("-------- Animal 2--------")
cat = Cat("Rose")
print(cat.name)
cat.sleep()
cat.eat()
cat.speek()
print("----------------------")
print()
print("-------- Animal 3--------")
mouse = Mouse("Hanafy")
print(mouse.name)
mouse.sleep()
mouse.eat()
mouse.speek()
print("----------------------")
print("######################################################")
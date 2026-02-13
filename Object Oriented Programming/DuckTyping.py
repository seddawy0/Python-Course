# Another way to achive polymorphism besides inheritence 
# Object must have the minimum necessary attributes/methods
# If it looks like a duck and quacks like a duck, it must be a duck


print("#################### Duck Typing #####################")
class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    def speak(self):
        print("MEOW")
        
class Car: # it has the minimum necessary attributes/methods
    alive = False # Because it is not a child of the Animal class, I must add this one  
    def speak(self): # name of the method is the same as the dog and the cat
        print("BEEB")
        
animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
print("######################################################")
# Multiple Inheritance = Inheret from more than one parent class
#                        C(A, B)

# Multilevel Inheritance = Inheret from a parent which inherets from another parent
#                        C(B) <- B(A) <- A


print("#################### Multiple Inheritance #####################")
class Animal: # Multilevel (Grandpa)
    def __init__(self, Name):
        self.name = Name
    
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal): # Parent
    def flee(self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey): # Child
    pass
class Hawk(Predator): # Child
    pass
class Fish(Prey, Predator): # Multiple  (Child)
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")
print("------- Rabbit -------")
rabbit.flee()
rabbit.eat()
rabbit.sleep()
print()
print("-------- Hawk --------")
hawk.hunt()
hawk.eat()
hawk.sleep()
print()
print("-------- Fish --------")
fish.flee()
fish.sleep()
fish.hunt()
fish.eat()
print("###############################################################")

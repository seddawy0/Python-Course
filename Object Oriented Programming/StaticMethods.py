# A method that belong to a class rather than any object from that class
# Usually used for general utility functions

# Instance = Best for operations on instances of the class (objects)
# Statics = Best for utility functions that don't need access to class data 

print("#################### Static Method #####################")
class Employee:
    def __init__(self, Name, Position):
        self.name = Name
        self.position = Position
    
    # Instance Method
    def getInfo(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod # Static Method
    def isValidPosition(Position):
        validPositions = ["Manager", "Cashier", "Chief", "Janitor"]
        return Position in validPositions
    
employee1 = Employee(Name="Mr.Crab", Position="Manager") # Instance
employee2 = Employee(Name="Squidward", Position="Cashier") # Instance
employee3 = Employee(Name="Spongebob", Position="Chief") # Instance
print(employee1.getInfo())
print(employee2.getInfo())
print(employee3.getInfo())
print("-------------------------------")
print(Employee.isValidPosition("Manager")) # Static
print(Employee.isValidPosition("President")) # Static
print("########################################################")

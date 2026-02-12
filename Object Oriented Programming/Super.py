# Function used in a child class to call methods from a parent class (superclass)
# Allows you to extend the functionality of the inherited methods

print("#################### Super() #####################")
class Shape:
    def __init__(self, Color, isFilled):
        self.color = Color
        self.isfilled = isFilled
        
    def describe(self):
        print(f"It is {self.color} and {'Filled' if self.isfilled else 'Not filled'}")

class Circle(Shape):
    def __init__(self, Color, isFilled, Radius):
        super().__init__(Color, isFilled)
        self.radius = Radius
    def describe(self):
        super().describe()
        print(f"It is a circle with area of {3.14 * self.radius ** 2}cm²")
        
class Square(Shape):
    def __init__(self, Color, isFilled, Width):
        super().__init__(Color, isFilled)
        self.width = Width
    def describe(self):
        super().describe()
        print(f"It is a square with area of {self.width ** 2}cm²")
        
class Triangle(Shape):
    def __init__(self, Color, isFilled, Width, Height):
        super().__init__(Color, isFilled)
        self.width = Width
        self.height = Height
    def describe(self):
        super().describe()
        print(f"It is a triangle with area of {self.width * self.height / 2}cm²")

circle = Circle(Color="Black", isFilled=True, Radius= 8)
square = Square(Color="Blue", isFilled=False, Width= 5)
triangle = Triangle(Color="Yellow", isFilled=True, Width= 7, Height= 9)

print("------- Circle -------")
circle.describe()
print()

print("------- Square -------")
square.describe()
print()

print("------- Triangle -------")
triangle.describe()

print("##################################################")

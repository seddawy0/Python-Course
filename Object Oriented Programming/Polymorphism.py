# Greek word that means to "have many forms or faces"


print("#################### Polymorphism #####################")
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, Radius):
        self.radius = Radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, Side):
        self.side = Side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, Base, Height):
        self.base = Base
        self.height = Height
    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, Topping, Radius):
        super().__init__(Radius)
        self.topping = Topping
    
shapes = [Circle(5), Square(5), Triangle(7,9), Pizza("Cheese", 7)]
shapeNum = 0
for shape in shapes:
    shapeNum += 1
    print(f"{shapeNum}- {shape.area()}cm²")
print("#######################################################")

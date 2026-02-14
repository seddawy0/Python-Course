# Decorator used to define a method as a property (it can be accessed like an attribute)
# Benifits: Add additional logic when read, write, or delete attributes
# Gives you getter, setter, and deleter methods


print("#################### Property #####################")
class Rectangle:
    def __init__(self, width, height):
        self._width = width # _width means it will be protected & internal
        self._height = height # _height means it will be protected & internal
    
    @property # Add additional logic when reading new attributes
    def width(self):
        return f"{self._width:.1f}cm"
    @property # Add additional logic when reading new attributes
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter # Add additional logic when writing/changing new attributes
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero!")
    @height.setter # Add additional logic when writing/changing new attributes
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero!")
    @width.deleter # Add additional logic when deleting new attributes
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter # Add additional logic when deleting new attributes
    def height(self):
        del self._height
        print("Height has been deleted")

print("------------- Getter Method -------------")
rectangle1 = Rectangle(4, 6)
print(rectangle1.width)
print(rectangle1.height)
print(rectangle1._width)
print(rectangle1._height)
print()

print("------------- Setter Method -------------")
rectangle1.width = 0
rectangle1.height = 10
print(rectangle1.width)
print(rectangle1.height)
print(rectangle1._width)
print(rectangle1._height)
print()

print("------------- Deleter Method -------------")
del rectangle1.width
del rectangle1.height
print()
print("###################################################")
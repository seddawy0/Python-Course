# A file containing code you want to include in your program
#   Use 'import' to include a module (built in or your own)
#   Useful to break up a large program reusable separate files
# We can refer to the name of a module with any name we want like
#                                                               import math as m
import ExampleModule
print("#################### Modules #####################")
# print(help("modules"))
# print(help("math"))
# Examples
print("-------------------- Example 1 ---------------------")
result = ExampleModule.pi
print(f"PI: {result}")
result = ExampleModule.square(5)
print(f"Square: {result}")
result = ExampleModule.cube(5)
print(f"Cube: {result}")
result = ExampleModule.circumference(5)
print(f"Circumference: {result}")
result = ExampleModule.circleArea(5)
print(f"Circle area: {result}")
print("-------------------- Example 1 ---------------------")
print("##################################################")
import math
print("################### Exercise 1 ####################")
# Calculate the circumference of a circle using this formula: C = 2πr
radius = float(input("Enter the radius of the circle (in cm): "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle, with radius = {radius}cm, is: {round(circumference, 2)}cm")
print("###################################################")
print()
print("################### Exercise 2 ####################")
# Calculate the area of a circle using this formula: A = πr²
radius = float(input("Enter the radius of the circle (in cm): "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle, with radius = {radius}cm², is: {round(area, 2)}cm²")
print("###################################################")
print()
print("################### Exercise 3 ####################")
# Calculate the hypotenuse of a triangle using this formula: c = √a²+b²
a = float(input("Enter the length of the side a (in cm): "))
b = float(input("Enter the length of the side b (in cm): "))
c = math.sqrt((pow(a, 2) + pow(b, 2)))
print(f"Side c is: {c}cm")
print("###################################################")
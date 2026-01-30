# Single variable used to store multiple variables
# List = [] Ordered & Changeable. Duplicates Ok
# Set = {} Unordered & Immutable, but Add/Remove Ok. No Duplicates
# Tuple = () Ordered & Unchangeable. Duplicates Ok. FASTER

print("#################### List ####################")
# Lists []
fruits = ["Apple", "Banana", "Coconut", "Mango"]
# print(dir(fruits))
# print(help(fruits))
print(fruits)
print(fruits[0])
print(fruits[::-1])
print("Pineapple" in fruits)
print("-----------------------------------")
for fruit in fruits:
    print(fruit, end="-")
print()
print("-----------------------------------")
fruits[0] = "Pineapple"
fruits.append("Strawberry")
print("-----------------------------------")
for fruit in fruits:
    print(fruit, end="-")
print()
print("-----------------------------------")
fruits.sort()
print("-----------------------------------")
for fruit in fruits:
    print(fruit, end="-")
print()
print("-----------------------------------")
print(fruits.index("Banana"))
print(fruits.count("Strawberry"))
print("##############################################")
print()
print()
print("#################### Set #####################")
# Sets {}
fruits = {"Apple", "Banana", "Coconut", "Mango"}
# print(dir(fruits))
# print(help(fruits))
print(fruits)
fruits.add("Apple")
fruits.remove("Banana")
print("-----------------------------------")
for fruit in fruits:
    print(fruit, end="-")
print()
print("-----------------------------------")
print("##############################################")
print()
print()
print("################### Tuple ####################")
# Tuple ()
fruits = ("Apple", "Banana", "Coconut", "Mango")
# print(dir(fruits))
# print(help(fruits))
print(fruits)
print(fruits[0])
print(fruits[::-1])
print(fruits.index("Banana"))
print(fruits.count("Strawberry"))
print("-----------------------------------")
for fruit in fruits:
    print(fruit, end="-")
print()
print("-----------------------------------")
print("##############################################")
# *args = Allows you to pass multiple non-key arguments. It will be a tuple
# **kwargs = Allows you to pass multiple keywork arguments. It will be a dictionary
# *Unpacking operator
print("#################### *Args & **Kwargs Arguments #####################")
# Args Examples 
print("##################### *Args #####################")
print("-------------------- Example 1 ---------------------")
def add(*numbers): # (*) You can change the name after the unpacking operator
    total = 0
    for number in numbers:
        total += number
    return total
print(f"Total: {add(5, 5, 5, 5, 6, 6, 6, 6)}")
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
def displayName(*args): # (*) Gives you a tuple 
    for arg in args:
        print(arg, end=" ")
displayName("Eng.", "Ziad", "Maged", "Bayoumy", "Abdelfattah", "Hassan", "Elsedawy")
print()
print("-------------------- Example 2 ---------------------")
print("##################### *Args #####################")
print()

# Kwargs Examples 
print("##################### **Kwargs #####################")
print("-------------------- Example 1 ---------------------")
def displayAddress(**kwargs): # (**) Gives you a dictionary 
    for key, value in kwargs.items():
        print(f"{key}: {value}")
displayAddress(Country= "Egypt",
               City= "Cairo",
               Street= "Zamzam",
               Zip= "14531")
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
def displayInfo(*args, **kwargs): 
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
displayInfo("Eng.", "Ziad", "Maged", "Bayoumy", "Abdelfattah", "Hassan", "Elsedawy",
            Country= "Egypt",
            City= "Cairo",
            Street= "Zamzam",
            Zip= "14531")
print("-------------------- Example 2 ---------------------")
print("##################### **Kwargs #####################")
print("#####################################################################")
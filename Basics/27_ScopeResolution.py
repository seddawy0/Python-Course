# Variable scope = Where a variable is visible and accessible
# Scope resolution = (LEGB) Local --> Enclosed --> Global --> Built-in
print("#################### Scope Resolution #####################")
# Examples
print("--------------------- Local -----------------------")
def func1():
    x = 1 # Local variable.
    print(x)
def func2():
    x = 5 # Local variable.
    print(x)
func1()
func2()
print("--------------------- Local -----------------------")
print()
print("------------------- Enclosed ---------------------")
def func1():
    x = 3 # Enclosed variable.
    def func2():
        # x = 5 # Local variable.
        print(x)
    func2()
func1()
print("------------------- Enclosed ---------------------")
print()
print("-------------------- Global ----------------------")
def func1():
    # x = 1 # Local variable.
    print(x)
def func2():
    # x = 5 # Local variable.
    print(x)
x = 4 # Global variable.
func1()
func2()
print("-------------------- Global ----------------------")
print()
print("------------------- Built-in ---------------------")
from math import e
print(e) # e is built-in
def func1():
    # e = 10 # Local
    print(e) 
# e = 20 # Global
print("------------------- Built-in ---------------------")
print("###########################################################")
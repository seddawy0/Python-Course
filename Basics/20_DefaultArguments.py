# A default value for certain parameters 
# Default is used when that argument is omitted
# Makes your function more flexible, reduce num of arguments
print("#################### Default Arguments #####################")
# Examples
print("-------------------- Example 1 ---------------------")
def netPrice(listPrice, discount = 0, tax = 0.02): # Default value after = sign 
    return listPrice * (1 - discount) * (1 + tax)
print(netPrice(250000))
print(netPrice(250000, 0.05, 0)) # You can change the default values 
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
import time
def counter(end, start = 0): # Non-Default arguments must be before default arguments
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Ended!")
counter(15)
counter(20, 15)
print("-------------------- Example 2 ---------------------")
print("############################################################")
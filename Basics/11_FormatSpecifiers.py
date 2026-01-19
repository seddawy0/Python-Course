# {value:flags} format a value based on what flags are inserted

print("################### Format Specifiers ####################")
print("----Prices----")
price1 = 3.14159
price2 = -987.5764
price3 = 55.9
price4 = 79.99
price5 = -100.1
price6 = 99.99
price7 = 1000000000
price8 = -1020050070
print(f"Price 1 is: ${price1:.1f}")
print(f"Price 2 is: ${price2:.2f}")
print(f"Price 3 is: ${price3:.3f}")
print(f"Price 4 is: ${price4:+}")
print(f"Price 5 is: ${price5: }")
print(f"Price 6 is: ${price6: }")
print(f"Price 7 is: ${price7:,}")
print(f"Price 8 is: ${price8:+,.2f}") # Mixed Flags
print("--------------")
print()
print("----Spaces----")
space1 = 3.14159
space2 = -987.5764
space3 = 55.9
space4 = 20.56
space5 = 30.87
space6 = 40.50
print(f"Space 1 is: {space1:10}")
print(f"Space 2 is: {space2:010}")
print(f"Space 3 is: {space3:<10}")
print(f"Space 4 is: {space4:>10}")
print(f"Space 5 is: {space5:<010}")
print(f"Space 6 is: {space6:^10}") # Centered
print("--------------")
print("##########################################################")
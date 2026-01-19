# A one-line shortcut for the if-else statement
#                                              X if condition else Y

print("################### Examples ####################")
# Positive or Negative 
print("----------------------------------")
num = float(input("Enter a number: "))
print("Positive" if num > 0 else "Negative")
print("----------------------------------")
print()
# Even or Odd
print("----------------------------------")
num0 = float(input("Enter a number: "))
print("Even" if num0 % 2 == 0 else "Odd")
print("----------------------------------")
print()
# Max or Min
print("----------------------------------")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
print(f"1st number {num1} is greater than the 2nd number {num2}" if num1 > num2 else f"2nd number {num2} is greater than the 1st number {num1}")
print("----------------------------------")
print()
# Status
print("----------------------------------")
age = int(input("Enter your age: "))
print("Adult" if age >= 18 else "Child")
print("----------------------------------")
print("#################################################")


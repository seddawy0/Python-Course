# Do some code only IF some or all conditions are true
#                                                     Else do something else

print("################### Example 1 ####################")
age = int(input("Enter your age: "))
if age >= 100:
    print("Your are too old to sign up!")
elif age >= 18:
    print("Your are now signed up!")
elif age < 0:
    print("You haven't been born yet!!")
else:
    print("You must be 18+ to sign up!")
print("##################################################")
print()
print("################### Example 2 ####################")
name = input("Enter your name: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")
print("##################################################")
print()
print("################### Example 3 ####################")
for_sale = True
if for_sale:
    print("The item is for sale!")
else:
    print("The item is not for sale!")
print("##################################################")
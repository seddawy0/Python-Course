# Execute a block of code a fixed number of times

print("################### For Loop ####################")
# Examples
print("----Example 1----")
for x in range(1, 11):
    print(x)
print("^^^^^^^^^^^^^^^^^")
for x in reversed(range(1, 16)):
    if x == 13: 
        continue # SKIP NUMBER 13
    else:
        print(x)
print("HAPPY NEW YEAR!")
print("-----------------")
print()
print("----Example 2----")
creditCard = "1234-5678-9012-3456"
for num in creditCard:
    print(num)
print("-----------------")
print()
print("----Example 3----")
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits: 
    print(f"I like {fruit}")
print("-----------------")
print()
print("----Example 4----")
for i in range(5):
    print("Welcome to Python!")
print("#################################################")
# A block of reusable code
print("#################### Functions #####################")
# Example 1
print("-------------------- Example 1 ---------------------")
def happyBirthday(name, age):
    print(f"Happy birth day {name}!")
    print(f"You are {age} year/s old now!")
    print("Happy birth day to you!")
happyBirthday("Seddawy", 19)
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
def displayInvoice(username, bill, dueDate):
    print(f"Hello {username},")
    print(f"Your bill of ${bill:.2f} is due: {dueDate}")
displayInvoice("Seddawy", 62.79, "15/2/2026")
print("-------------------- Example 2 ---------------------")
print()
print("##################### Return #####################")
# A statement used to end a function and send the result back to the caller
print("-------------------- Example 1 ---------------------")
def add(num1, num2):
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
    return total
def subtract(num1, num2):
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")
    return total
add(5, 2)
subtract(10, 2)
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
def displayFullName(firstName, lastName):
    print(f"Your full name is: {firstName.capitalize()} {lastName.capitalize()}")
    return firstName, lastName
displayFullName("ziad", "elsedawy")
print("-------------------- Example 2 ---------------------")
print("##################### Return #####################")
print("####################################################")
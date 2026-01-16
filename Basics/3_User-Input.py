# input() : A function that prompts the user to enter data
# Returns the entered data as a string

print("######################### Input ###########################")
# Input
username = input("Enter your username: ")
age = int(input("Enter your age: ")) # Convert it to an integer so you can do math to the integer without errors
gpa = float(input("Enter your GPA: "))
print("-----------------------------------------------------------")
print(f"Hello {username}!")
print(f"You are {age} years old")
print(f"Your GPA is: {gpa}")
print("###########################################################")
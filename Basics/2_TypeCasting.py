# The Process of converting a variable from one data type to another {str(), int(), float(), bool()}

print("######################### Type of the variable before converting ###########################")
# Type of the variable before converting
username = "Seddawy0"
age = 19
gpa = 3.5
is_student = True
print(type(username))
print(type(age))
print(type(gpa))
print(type(is_student))
print("############################################################################################")
print()
print("################################ Converting the variable ###################################")
# Converting the variable
username = bool(username)
age = float(age)
gpa = int(gpa)
is_student = str(is_student)
print(username)
print(age)
print(gpa)
print(is_student)
print("############################################################################################")
print()
print("######################### Type of the variable after converting ############################")
# Type of the variable after converting
print(type(username))
print(type(age))
print(type(gpa))
print(type(is_student))
print("############################################################################################")
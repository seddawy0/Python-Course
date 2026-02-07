# Used to test whether a value or variable is found in a sequence 
#                                                       (String, list, set, tuple, dictionary)
# in & not in
print("#################### Membership Operators #####################")
# Examples
print("-------------------- Example 1 ---------------------")
word = "BANANA"
letter = input("Guess a letter in a secret word: ")
if letter.upper() in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
print("-------------------- Example 1 ---------------------")
print()
print("-------------------- Example 2 ---------------------")
# Lists, Sets, Tuples
students = ("Ziad", "Maged", "Sandy", "Roka")
student = input("Enter the name of the student: ").title()
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")
print("-------------------- Example 2 ---------------------")
print()
print("-------------------- Example 3 ---------------------")
# Dictionary
grades = {"Ziad": "A",
          "Maged": "A",
          "Sandy": "C",
          "Roka": "B"}
student = input("Enter the name of the student: ").title()
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
print("-------------------- Example 3 ---------------------")
print()
print("-------------------- Example 4 ---------------------")
email = "seddawy0@gmail.com"
if "@" in email and "." in email:
    print(f"{email} is a valid email")
else:
    print(f"{email} is NOT a valid email")
print("-------------------- Example 4 ---------------------")
print("################################################################")
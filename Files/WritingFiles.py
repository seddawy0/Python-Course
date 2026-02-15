# Python writing files (.txt, .json, .csv)
# with = Automatically closes the file after finishing it
# open() = A function asks for a permession to work on the file
# mode = {"r": Read, "w": Write, "a": Append, "x": Create (create file if not exists, error if exists)}
print("##################### Writing Files ######################")
import json
import csv

text_data = "Ziad El-Sedawy was here!"
file_path = "C:/Users/zsedd/Desktop/Output.txt"

try:
    with open(file=file_path, mode="a") as file:
        file.write("\n" + text_data)
        print(f"txt file '{file_path}' has been created")
except FileNotFoundError:
    print("That path doesn't exist!")
print("-----------------------------------------------------")
print()
students = ["Ziad El-Sedawy", "Ahmed Khaled", "Abdelghany Ashraf", "Ziad Ahmed", "Hamza Mohamed"]
file_path = "C:/Users/zsedd/Desktop/Students.txt"
try:
    with open(file=file_path, mode="w") as file:
        student_num = 0
        for student in students:
            student_num +=1
            file.write(f"{student_num}- {student}\n")
        print(f"txt file '{file_path}' has been created")
except FileNotFoundError:
    print("That path doesn't exist!")
print("-----------------------------------------------------")
print()
students = {"name": ["Ziad El-Sedawy", "Ahmed Khaled", "Abdelghany Ashraf", "Ziad Ahmed", "Hamza Mohamed"],
            "age": [19, 19, 18, 18, 16],
            "grade": [12, 12, 12, 12, 10]}
file_path = "C:/Users/zsedd/Desktop/Students.json"
try:
    with open(file=file_path, mode="w") as file:
        json.dump(students, file, indent=4)
        print(f"Json file '{file_path}' has been created")
except FileNotFoundError:
    print("That path doesn't exist!")
print("-----------------------------------------------------")
print()
students = [["Name", "Age", "Grade"],
            ["Ziad El-Sedawy", 19, 12],
            ["Ahmed Khaled", 19, 12],
            ["Abdelghany Ashraf", 18, 12],
            ["Ziad Ahmed", 18, 12],
            ["Hamza Mohamed", 16, 10]]
file_path = "C:/Users/zsedd/Desktop/Students.csv"
try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # for row in students: # It is slow
        #     writer.writerow(row) 
        writer.writerows(students) # It is faster
        print(f"Csv file '{file_path}' has been created")
except FileNotFoundError:
    print("That path doesn't exist!")
print("-----------------------------------------------------")
print("##########################################################")
# Python reading files (.txt, .json, .csv)
# with = Automatically closes the file after finishing it
# open() = A function asks for a permession to work on the file
# mode = {"r": Read, "w": Write, "a": Append, "x": Create (create file if not exists, error if exists)}
print("##################### Reading Files ######################")
import json
import csv
file_path = "C:/Users/zsedd/Desktop/Output.txt"
try:
    with open(file=file_path, mode="r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You don't have permission to read that file!")
print("-----------------------------------------")
print()
file_path = "C:/Users/zsedd/Desktop/Students.json"
try:
    with open(file=file_path, mode="r") as file:
        data = json.load(file)
        print(data["name"])
        print(data["age"])
        print(data["grade"])
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You don't have permission to read that file!")
print("-----------------------------------------")
print()
file_path = "C:/Users/zsedd/Desktop/Students.csv"
try:
    with open(file=file_path, mode="r") as file:
        data = csv.reader(file)
        line_num = 0
        for line in data:
            print(" | ".join(line))
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You don't have permission to read that file!")
print("##########################################################")
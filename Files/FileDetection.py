# Relative file path = folder/filename
# Absolute file path = C:/Users/seddawy/folder/filename 
#                   OR C:\\Users\\seddawy\\folder\\filename 
print("##################### File Detection ######################")
# File Detection
import os
base_dir = os.path.dirname(__file__) 
file_path = os.path.join(base_dir, "test1.txt")
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does't exist")
print("-----------------------------------------")
file_path = os.path.join(base_dir, "Stuff/test2.txt")
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does't exist")
print("-----------------------------------------")
file_path = os.path.join(base_dir, "Stuff/test2")
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does't exist")
print("-----------------------------------------")
file_path = os.path.join(base_dir, "Stuff")
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does't exist")
print("-----------------------------------------")
file_path = "D:/Work/Python/Files/test1.txt"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location does't exist")
print("###########################################################")
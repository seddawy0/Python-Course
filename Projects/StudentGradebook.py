print("######################### Student Gradebook ###########################")
# Student Gradebook V1
students = []
grades = []
########################### Logic #############################
while True:
    student = input("Enter student's name (q to quit): ")
    while student == "":
        student = input("Enter student's name (q to quit): ")
    if student.lower() == "q":
        break
    grade_input = input("Enter student's grade: ")
    while grade_input == "":
        grade_input = input("Enter student's grade: ")
    grade = float(grade_input)
    students.append(student)
    grades.append(grade)
if len(students) > 0:
    average = sum(grades) / len(students)
    maxGrade = max(grades)
    minGrade = min(grades)
    maxGradeIndex = grades.index(max(grades))
    minGradeIndex = grades.index(min(grades))
    print()
    print("---------- Student: Grade ----------")
    for i in range(len(students)):
        print(f"{students[i]}: {grades[i]}")
    print("------------------------------------")
    print(f"Average grade: {average:.2f}")
    print(f"Top Student: {students[maxGradeIndex]} with {maxGrade}")
    print(f"Needs Improvement: {students[minGradeIndex]} with {minGrade}")
else:
    print("No students were entered.")
###############################################################
print("#######################################################################")

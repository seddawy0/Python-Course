# Shared among all instances of a class
#                 Defined outside the constructor
#                 Allow you to share data among all objects created from that class


print("#################### Class Variables #####################")
class Students:
    classYear = 2026
    numOfStudents = 0
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
        Students.numOfStudents += 1

# Objects
student1 = Students("Ziad Elsedawy", 19)
student2 = Students("Solaiman Elhalaby", 18)
student3 = Students("Eyad Tarek", 17)
print(f"My graduating class of {Students.classYear} has {Students.numOfStudents} students:")
print(student1.name)
print(student2.name)
print(student3.name)
print("##########################################################")
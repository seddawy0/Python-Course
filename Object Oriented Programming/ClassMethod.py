# Allows operations related to the class itself
# take (cls) as the first parameter, which represents the class itself

# Instance = Best for operations on instances of the class (objects)
# Statics = Best for utility functions that don't need access to class data 
# Class = Best for class-level data or require access to the class itself

print("#################### Class Method #####################")
class Student:
    counter = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.counter += 1
        Student.total_gpa += gpa
    def get_info(self):
        return f"{self.name}: {self.gpa}"
    
    @classmethod
    def number_of_students(cls):
        return f"Total # of students: {cls.counter}"
    @classmethod
    def average_gpa(cls):
        if cls.counter == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.counter:.2f}"
    
student1 = Student(name="Ziad Elsedawy", gpa=3.8)
student2 = Student(name="Patrick", gpa=2.0)
student3 = Student(name="Sandy", gpa=3.6)

print(Student.number_of_students())
print(Student.average_gpa())
print("#######################################################")

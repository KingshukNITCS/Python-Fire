# student.py (Module)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")



# main.py (Module)
from student import Student

# Creating instances of the Student class
student1 = Student(name="Alice", age=20)
student2 = Student(name="Bob", age=22)

# Displaying information using the class method
student1.display_info()
student2.display_info()




# teacher.py (Module)
class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")
      


# student.py (Updated Module)
from teacher import Teacher  # Importing the Teacher class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Intern(Student, Teacher):  # Inheriting from both Student and Teacher
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Role: {self.role}")

'''
Organizing with Packages:
As projects grow, organizing modules into packages becomes crucial. Let's organize our existing modules into a package named school.

school/

├── __init__.py

├── student.py

├── teacher.py

└── main.py

The __init__.py file signifies that the school directory is a Python package. Now, we can update our main.py to import classes from the school package.
'''
# main.py (Updated)
from school.student import Student, Intern
from school.teacher import Teacher

# ... (rest of the code remains the same)


class Person:
  name = "Deepika"
  city = "Mumbai"

p1=Person()
print(p1.name)
print(p1.city)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Person:
  name = "Deepika"
  city = "Mumbai"

p1=Person()
p1.name = "Rose"
print(p1.name)


# Delete the age property from the p1 object:
class Person:
  name = "Deepika"
  city = "Mumbai"
  age = 20

p1=Person()
del p1.age


# delete objects by using the del keyword.
class Person:
  name = "Deepika"
  city = "Mumbai"

p1=Person()
del p1
print(p1.name)


# Encapsulation and Modularity
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# Polymorphism in Action. Polymorphism allows objects to be treated as instances of their parent class, enabling flexibility in handling various data types. This concept is particularly useful in scenarios where the same operation can be applied to different types of objects.
def describe(animal):
    animal.make_sound()

# Usage
dog = Dog("Woof")
cat = Cat("Whiskers")

describe(dog)  # Output: Woof!
describe(cat)  # Output: Meow!

  
# Relevance to Data Science: Structuring Data with Classes
# In the context of data science, classes provide a powerful way to structure and organize data. For example, you might create a class to represent a dataset, with attributes for columns and methods for data analysis.

class DataSet:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        # Perform data analysis here
        pass




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



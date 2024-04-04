# Syntax Error

# initialize the amount variable 
amount = 10000

# check that You are eligible to 
if(amount>2999) 
	print("Item approved") 

# Logical Errors
total = 5 - 4# Logical Error
print("Total is:", total)  # Expected output: Total is 9 (mistakenly prints 1)


# Runtime Error
result = 10 / 0 #ZeroDivisionError

total = "5" + 5 #TypeError


# IndexError
my_list = [1, 2, 3]
value = my_list[5]

# ValueError
age = int("twenty")

# FileNotFoundError
with open("nonexistent_file.txt", "r") as file:
    content = file.read()

# KeyError
my_dict = {"name": "Alice", "age": 30}
value = my_dict["gender"]

# AttributeError
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Bob")
age = person.age

# ImportError
import non_existent_module

	

#creating a function to calculate area of circle
def calculate_area(radius):
    area = 3.14 * radius**2
    return area

#calling the user-defined function
circle_area = calculate_area(5)
print(circle_area)


# Functions can have default parameter values. If a value for a parameter is not provided during the function call, the default value is used.

def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message
print(greet("Geeks"))


# Passing keyword arguments allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.

def student(firstname, lastname):
	print(firstname, lastname)

# Keyword arguments
student(firstname='Python', lastname='Programmer')
student(lastname='Programmer', firstname='Python')

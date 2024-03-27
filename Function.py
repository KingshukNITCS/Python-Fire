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


# Python supports variable-length arguments through *args and **kwargs. This allows a function to accept a flexible number of arguments.

def print_values(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_values(1, 2, 3, name="Rose", age=24)


# In Python, a nested function is a function defined inside another function. The inner function has access to the variables of the outer (enclosing) function, and it can use them even after the outer function has finished execution. This concept is known as "closure".

def func_1(x):
    S = "Data Science with Python"
    def func_2():
        return (S,x)
    return func_2()

# Create a closure
closure = func_1(3.0)

print(closure)


# Recursive


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result) 


# Problem Statement - Calculating the nth term of the Ackermann function.
# The Ackermann function is a recursive mathematical function that is exceptionally fast-growing. It is often used to demonstrate the difference in growth rates between simple recursive algorithms and more efficient ones.

# If m = 0, the result is n + 1.

# If m > 0 and n = 0, the result is ackermann(m-1, 1).

# If m > 0 and n > 0, the result is ackermann(m-1, ackermann(m, n-1)).

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))

result = ackermann(3, 4)
print(result)  

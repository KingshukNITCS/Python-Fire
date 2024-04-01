# Using dictionary comprehension to create a dictionary of squared even numbers
numbers = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(numbers)

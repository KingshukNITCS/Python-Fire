# Zip function is used to combine multiple iterables (e.g., lists, tuples) element-wise, creating tuples containing elements from the input iterables.
tuple1 = (1, 4, 8)
List1 = ["Geeks" , "for", "Geeks", "Python"]
zipped_data = zip(tuple1, List1)
print(list(zipped_data))
# Output - [(1, 'Geeks'), (4, 'for'), (8, 'Geeks')]


# Filter function in python is used to construct an iterator from elements of an iterable for which a function returns True. It filters out elements based on a specified condition. If the condition is satisfied and True is returned, it's not filtered out. If the condition isn't satisfied and False is returned, the element of the iterable is filtered out.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(number):
    return number%2==0
filtered_numbers = list(filter(is_even, numbers))
print(filtered_numbers)
# Output - [2, 4, 6, 8, 10]


# Lambda functions (or anonymous functions) are small, anonymous functions defined using the lambda keyword. They are often used for short-term operations where a full function definition is unnecessary.

# Syntax: lambda arguments : expression

# 1. Lambda function with List Comprehension

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
	print(item(), end = ' ')
# Output - 10 20 30 40

# 2. Lambda function with conditional statements

Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))
# Output - 2


# 3. Lambda function with filter()

programming_languages = ["C", "C++", "Java", "Python", "JavaScript", "Ruby", "Swift"]

# Using filter with lambda to filter strings containing "Python"
java_languages = list(filter(lambda lang: "Java" in lang, programming_languages))

print("Programming Languages:", programming_languages)
print("Languages containing 'Java':", java_languages)

'''
Output - Programming Languages: ['C', 'C++', 'Java', 'Python', 'JavaScript', 'Ruby', 'Swift']

Languages containing 'Java': ['Java', 'JavaScript']
'''


# Map function in python
'''
map function applies a given function to all items in an input iterable (e.g., list) and returns an iterator of the results.

syntax: map(function, iterable, ...)
'''

numbers = [1, 2, 3, 4, 5]
# Using map to square each element
squared_numbers = map(lambda x: x**2, numbers)

result_list = list(squared_numbers)
print(result_list)
# Output - [1, 4, 9, 16, 25]


# Combining all functions

names = ["Geeks", "For", "Geeks"]
scores = [25, 30, 22]

filtered_names = list(filter(lambda x: len(x) > 4, names))
uppercase_names = list(map(lambda x: x.upper(), filtered_names))

zipped_data = list(zip(uppercase_names, scores))
print(zipped_data)
# Output - [('GEEKS', 25), ('GEEKS', 30)]



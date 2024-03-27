# A Python module is created by saving Python code in a file with a extension. For example, let's create a simple module named 
# Module - list_operations

def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]

def reverse_list(input_list):
    return input_list[::-1]

def concatenate_lists(list1, list2):
    return list1 + list2


# Once a module is created, it can be imported into other Python scripts or modules. There are several ways to import a module:

# Importing the Entire Module

import list_operations
avg = list_operations.find_average([5, 3, 4, 7])
evens = list_operations.filter_even([5, 3, 4, 7])
print(avg,evens)  


# Importing Specific Functions

from list_operations import filter_even
evens = filter_even([3,5,6,7,8,0])

print(evens)      



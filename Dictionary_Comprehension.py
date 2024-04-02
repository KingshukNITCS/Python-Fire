# Using dictionary comprehension to create a dictionary of squared even numbers
numbers = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(numbers)

# Creating a dictionary from Lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(result)

# Nested dictionary comprehension
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(2, 6)} for k1 in range(5, 7)
}
print(dictionary)

# Problem Statement - Find Common Elements from the given multiple Lists.


def find_common_elements(lists):
    common_elements = {element: min(lst.count(element) for lst in lists) for element in set.intersection(*map(set, lists))}
    return common_elements

list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 4, 4, 5]
list3 = [3, 4, 5, 5, 6]

result = find_common_elements([list1, list2, list3])

for element, frequency in result.items():
    print(f"Element: {element}, Frequency: {frequency}")


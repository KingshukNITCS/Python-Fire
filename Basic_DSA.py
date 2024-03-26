# List Example
items_list = ['apple', 'banana', 'orange', 5]

# Tuple Example
fruit_tuple = ('kiwi', 'grape', 'pear')


# Dictionary Example
person_info = {'Name': 'Sophie', 'Age': 28, 'Job': 'Scientist'}


# Quick Queue: Deque
# A deque is like a line where people can join or leave from both ends. This is handy when we need to manage information like a queue – first in, first out!


from collections import deque

# Creating a Deque
people_line = deque(['Alice', 'Bob', 'Charlie'])

# Joining and Leaving
people_line.append('David') #right
print(people_line)

people_line.popleft() #left
print(people_line)

people_line.pop() #right
print(people_line)

people_line.appendleft('Elon') #left
print(people_line)


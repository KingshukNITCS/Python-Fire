'''
Tuples are immutable which means once a tuple is created, you cannot modify its elements. You can't add, remove, or change elements in a tuple.
Tuples are ordered, meaning the position of an element in a tuple is preserved.
Tuples can contain elements of different data types. You can have integers, strings, floats, and other data types within the same tuple.
'''

my_tuple = (2, 4, "Python", 5.0, -3)
ele_1 = my_tuple[-2] 
ele_2 = my_tuple[2] 
print (ele_1, ele_2)


my_tuple = (1, 3, "Geeks", 4.0, "python", 1)
index= my_tuple.index('python') 
count = my_tuple.count(1) 
print (f"index of python: { index }, count of 1 : {count}")


packed_tuple = 1, 2, 'three' # in () also fine

# Tuple unpacking
a, b, c = packed_tuple
print (f" packed Tuple : {packed_tuple}, unpacked tuple a: {a}, b: {b}, c : {c}")

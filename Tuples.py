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

# Problem Statement - Two Sum Problem that returns a tuple of elements equal to given sum
def two_sum_tuples(nums, target):
    num_indices = {}  # Dictionary to store indices of elements

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_indices:
            return (complement, num)

        # Add the current element to the dictionary
        num_indices[num] = i

    return None  

nums = [2, 7, 11, 15]
target = 9
result = two_sum_tuples(nums, target)
print("Tuple of Elements:", result)


# Problem Statement 2 : Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_set = set()
    max_length = 0
    left_pointer = 0

    for right_pointer in range(len(s)):
        while s[right_pointer] in char_set:
            char_set.remove(s[left_pointer])
            left_pointer += 1

        char_set.add(s[right_pointer])
        max_length = max(max_length, right_pointer - left_pointer + 1)

    return max_length

input_str = "abcabcbb"
result = length_of_longest_substring(input_str)
print("Length of Longest Substring:", result)



l = ["Data", "Science", "Python"]
for i in l:
	print(i)



print("Dictionary Iteration")
d = dict()

d['key1'] = "val1"
d['key2'] = 345
for i in d:
	print(i, d[i])



#for loop with strings
word = "Python"

for letter in word:
    print(letter)
  



for i in range(5):
    print(i,end=' ')



for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
	

# Enumerate using For loop
# The enumerate() function is handy for obtaining both the index and value during iteration: 
# Output - 
# Index: 0, Subj: Data-Science
# Index: 1, Subj: Power BI
# Index: 2, Subj: Python

list1 = ["Data-Science", "Power BI", "Python"]

for index, subject in enumerate(list1):
    print(f"Index: {index}, Subj: {subject}")



#List Comprehensions:
squares = [x**2 for x in range(5)]
print(squares)


# Armstrong Problem

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_digits == number

# User input
num = int(input("Enter a number: "))

# Check and display the result
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
	

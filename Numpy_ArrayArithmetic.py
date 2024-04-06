'''
NumPy achieves its fast implementation using vectorization. One of the important features of NumPy arrays is that a developer can perform the same mathematical operation on every element with a single command.

Let us understand arithmetic operations using NumPy.
'''

import numpy as np
 
# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
 
# Performing addition using arithmetic operator
add_ans = a+b
print(add_ans)
 
# Performing addition using numpy function
add_ans = np.add(a, b)
print(add_ans)
 
# The same functions and operations can be used for multiple matrices
c = np.array([1, 2, 3, 4])
add_ans = a+b+c
print(add_ans)
 
add_ans = np.add(a, b, c)
print(add_ans)

'''
Output

[  7  77  23 130]
[  7  77  23 130]
[  8  79  26 134]
[  8  79  26 134]
As we can see that the matrixes are of the same shape, if they are different than, Numpy will try broadcasting if it is possible. The reader can see that the same operation (addition) can be done using arithmetic operation (+) as well as numpy function (np.add).
'''

import numpy as np
 
# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
 
# Performing subtraction using arithmetic operator
sub_ans = a-b
print(sub_ans)
 
# Performing subtraction using numpy function
sub_ans = np.subtract(a, b)
print(sub_ans)

'''
Output

[ 3 67  3 70]
[ 3 67  3 70]
'''

import numpy as np
 
# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
 
# Performing multiplication using arithmetic operator
mul_ans = a*b
print(mul_ans)
 
# Performing multiplication using numpy function
mul_ans = np.multiply(a, b)
print(mul_ans)

'''
Output

[  10  360  130 3000]
[  10  360  130 3000]
'''



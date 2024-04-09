'''
What is Numpythe ?

NumPy stands for Numerical Python. It is an Open Source Python library used for working with arrays. NumPy was created in 2005 by Travis Oliphant. It has functions for working in the domain of linear algebra, Fourier transform, and matrices.

Advantages of Numpy over Python List

NumPy provides an array object (ndarray) that is up to 70x faster than traditional Python lists. NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.This behavior is called locality of reference.This is the main reason why NumPy is faster than lists.

!pip install numpy

'''

import numpy as np

# Converting the Python Arrays into Numpy Arrays


lst = [1,2,3,4]
arr = np.array(lst)
print(arr)


# Creating Multidimensional Arrays


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr

'''
Arrange function : It creates an array by using the evenly spaced values over the given interval.

Syntax : numpy.arrange(start, stop, step, dtype) 

Where:

1 - start: The starting of an interval. The default is 0.

2- stop: represents the value at which the interval ends excluding this value.

3- step: The number by which the interval values change.

4- dtype: the data type of the numpy array items.

'''


arr = np.arange(1,10,2)


# Above code will create an array from 1 to 10 with the step of 2.

'''
Size Function : In Python, numpy.size() function count the number of elements along a given axis (0 - Rows | 1 - Columns)
'''

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])

print('Total : ', arr.size)
print('Rows  : ', np.size(arr,0))
print('Cols  : ', np.size(arr,1))


'''
Shape Function :  It used to find the dimensions of data ie no of rows and columns
'''

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])
print(arr.shape)

'''
dtype Function :dtype in Python usually means the data type of the elements of a numpy array.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
'''

arr1 = np.array([1,2,3,1,2,3])
arr2 = np.array([1.2,3.1,2.3])
print(arr1.dtype)
print(arr2.dtype)


'''
Ndim Function :The ndim attribute in NumPy provides the number of dimensions in an array ie 1-D , 2-D etc.
'''

arr1 = np.array([1,2,3,1,2,3])
arr2 = np.array([[1,2,3],[1,2,3]])

print(arr1.ndim)
print(arr2.ndim)

arr3 = np.array(arr1, ndmin = 3)
print(arr3.ndim)


'''
Zeros Function : returns an array with the given shape and data type filled with zeros.
'''

# Example 1: Create a 1D array of zeros
# With 7 elements and integer data type
arr = np.zeros(9)

# Example 2: Create a 1D array of zeros
# With 7 elements and integer data type
arr = np.zeros(7, int)

# Example 3: Create two-dimensional array with zeros
arr = np.zeros((4,5))

# Example 4: Create three-dimensional array with zeros
arr = np.zeros((4, 3, 5))



arr = np.zeros(shape = (3,5), dtype = int)
'''
Output : 
[[0 0 0 0 0]
[0 0 0 0 0]
[0 0 0 0 0]]
'''

'''
Ones function : used to create a new array of given shape and type, filled with ones.

Syntax : numpy.ones(shape, dtype = None)
'''

arr = np.ones(shape = (3,5), dtype = int)
print(arr)

Output : 
[[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]]


'''
Eye Function : The eye tool returns a 2-D array with 1’s as the diagonal and 0’s elsewhere. The diagonal can be main, upper, or lower .

Syntax : numpy.matlib.eye(n, m, dtype)

where : n :This parameter is used to represent the number of rows in the resulting matrix.

m :This parameter is used to represent the number of columns and the default value is n.

k:This parameter is used to indicate an index of diagonal,value of this parameter is 0 by default if value of k>0 it means diagonal is above the main diagonal or vice versa.

dtype :This parameter is used to indicate the data type of the matrix. The default value of this parameter is float. This is an optional parameter.
'''

np.eye(4, dtype = int)

'''
Output : 
array([[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, 1, 0],
[0, 0, 0, 1]])
'''

'''
Empty Function: It is used to create a new array of given shapes and types, without initializing entries.
'''


np.empty(shape = (5,5))


Output : 
array([[0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0.],
[0., 0., 0., 0., 0.]])

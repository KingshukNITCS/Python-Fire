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

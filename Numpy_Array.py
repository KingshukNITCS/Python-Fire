'''
Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.
Besides its obvious scientific uses, Numpy can also be used as an efficient multi-dimensional container of generic data.

 

If you do not have numpy installed in your system first you need to install it.


!pip install numpy

A list in Python is a linear data structure that can hold heterogeneous elements they do not require to be declared and are flexible to shrink and grow. On the other hand, an array is a data structure which can hold homogeneous elements, arrays are implemented in Python using the NumPy library. Arrays require less memory than list.

The similarity between an array and a list is that the elements of both array and a list can be identified by its index value.

 

Now let us convert a list into an array
'''
import numpy as np

l=[2,3,4,5]
print(l)
print(type(l))
print()
arr=np.array(l)
print(arr)
print(type(arr))


'''
Output: 

[2, 3, 4, 5]
<class 'list'>

[2 3 4 5]
<class 'numpy.ndarray'>
So we have first printed the list and then converted the list to an array and displayed that as well
'''

# numpy.ndarray.ndim() function return the number of dimensions of an array.

a=np.array([1,2,3,4])
b=np.array([[1,2,3,4],[5,6,7,8]])
print(a.ndim)
print(b.ndim)

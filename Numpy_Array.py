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
print(a.ndim) #1
print(b.ndim) #2


'''
Now we have few more functions such as np.array.shape, np.array.size and np.array.dtype

shape will basically return us the total number of rows and columns of the array in a tuple format (number of rows, number of columns)

size will tell us the total number of elements or values present in the array

dtype will tell us the data type of values which the array is containing
'''

b=np.array([[1,2,3,4],[5,6,7,8]])
print(b.shape) # (2,4)
print(b.size) # 8
print(b.dtype) # int32


'''

The numpy.zeros() function returns a new array of given shape and type, with zeros. Syntax:

numpy.zeros(shape, dtype = None, order = 'C')
Parameters :

 

shape : integer or sequence of integers
order  : C_contiguous or F_contiguous
         C-contiguous order in memory(last index varies the fastest)
         C order means that operating row-rise on the array will be slightly quicker
         FORTRAN-contiguous order in memory (first index varies the fastest).
         F order means that column-wise operations will be faster. 
dtype : [optional, float(byDeafult)] Data type of returned array.  
Returns : 

ndarray of zeros having given shape, order and datatype.

'''


# Python Program illustrating
# numpy.zeros method
 
import numpy as geek
 
b = geek.zeros(2, dtype = int)
print("Matrix b : \n", b)
 
a = geek.zeros([2, 2], dtype = int)
print("\nMatrix a : \n", a)
 
c = geek.zeros([3, 3])
print("\nMatrix c : \n", c)


'''
Output : 

Matrix b : 
 [0 0]

Matrix a : 
 [[0 0]
 [0 0]]

Matrix c : 
 [[ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]]
 '''

# Python Program illustrating
# numpy.ones method
 
import numpy as geek
 
b = geek.ones(2, dtype = int)
print("Matrix b : \n", b)
 
a = geek.ones([2, 2], dtype = int)
print("\nMatrix a : \n", a)
 
c = geek.ones([3, 3])
print("\nMatrix c : \n", c)

'''
Output : 
 

Matrix b : 
 [1 1]

Matrix a : 
 [[1 1]
 [1 1]]

Matrix c : 
 [[ 1.  1.  1.]
 [ 1.  1.  1.]
 [ 1.  1.  1.]]
'''

# The arange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval. The interval mentioned is half-opened i.e. [Start, Stop) 

# Python Programming illustrating
# numpy.arange method
 
import numpy as geek
 
print("A\n", geek.arange(4).reshape(2, 2), "\n")
print("A\n", geek.arange(4, 10), "\n")
print("A\n", geek.arange(4, 20, 3), "\n")

'''
Output : 

A
 [[0 1]
 [2 3]]

A
 [4 5 6 7 8 9]

A
 [ 4  7 10 13 16 19]
 '''

# The numpy.linspace() function returns number spaces evenly w.r.t interval. Similar to numpy.arange() function but instead of step it uses sample number

# Python Programming illustrating
# numpy.linspace method
 
import numpy as geek
 
# restep set to True
print("B\n", geek.linspace(2.0, 3.0, num=5, retstep=True), "\n")
 
# To evaluate sin() in long range
x = geek.linspace(0, 2, 10)
print("A\n", geek.sin(x))

'''
Output : 

B
 (array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)

A
 [ 0.          0.22039774  0.42995636  0.6183698   0.77637192  0.8961922
  0.9719379   0.99988386  0.9786557   0.90929743]
'''


'''
The numpy.reshape() function shapes an array without changing the data of the array.

Syntax:

numpy.reshape(array, shape, order = 'C')
'''
# Python Program illustrating
# numpy.reshape() method
 
import numpy as geek
 
# array = geek.arrange(8)
# The 'numpy' module has no attribute 'arrange'
array1 = geek.arange(8)
print("Original array : \n", array1)
 
# shape array with 2 rows and 4 columns
array2 = geek.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n",
      array2)
 
# shape array with 4 rows and 2 columns
array3 = geek.arange(8).reshape(4, 2)
print("\narray reshaped with 4 rows and 2 columns : \n",
      array3)
 
# Constructs 3D array
array4 = geek.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n",
      array4)

'''
Output : 

Original array : 
 [0 1 2 3 4 5 6 7]

array reshaped with 2 rows and 4 columns : 
 [[0 1 2 3]
 [4 5 6 7]]

array reshaped with 4 rows and 2 columns : 
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]

Original array reshaped to 3D : 
 [[[0 1]
  [2 3]]
 [[4 5]
  [6 7]]]
  
 
 [[0 1 2 3]
 [4 5 6 7]]
 '''


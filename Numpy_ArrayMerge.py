# Python program explaining
# vstack() function
  
import numpy as geek
  
# input array
in_arr1 = geek.array([ 1, 2, 3] )
print ("1st Input array : \n", in_arr1) 
  
in_arr2 = geek.array([ 4, 5, 6] )
print ("2nd Input array : \n", in_arr2) 
  
# Stacking the two arrays vertically
out_arr = geek.vstack((in_arr1, in_arr2))
print ("Output vertically stacked array:\n ", out_arr)
'''
Output:

1st Input array : 
 [1 2 3]
2nd Input array : 
 [4 5 6]
Output vertically stacked array:
  [[1 2 3]
 [4 5 6]]
 '''

# Python program explaining
# vstack() function
  
import numpy as geek
  
# input array
in_arr1 = geek.array([[ 1, 2, 3], [ -1, -2, -3]] )
print ("1st Input array : \n", in_arr1) 
  
in_arr2 = geek.array([[ 4, 5, 6], [ -4, -5, -6]] )
print ("2nd Input array : \n", in_arr2) 
  
# Stacking the two arrays vertically
out_arr = geek.vstack((in_arr1, in_arr2))
print ("Output stacked array :\n ", out_arr)

'''
Output:

1st Input array : 
 [[ 1  2  3]
 [-1 -2 -3]]
2nd Input array : 
 [[ 4  5  6]
 [-4 -5 -6]]
Output stacked array :
  [[ 1  2  3]
 [-1 -2 -3]
 [ 4  5  6]
 [-4 -5 -6]]
 '''


# Python program explaining
# hstack() function
  
import numpy as geek
  
# input array
in_arr1 = geek.array([ 1, 2, 3] )
print ("1st Input array : \n", in_arr1) 
  
in_arr2 = geek.array([ 4, 5, 6] )
print ("2nd Input array : \n", in_arr2) 
  
# Stacking the two arrays horizontally
out_arr = geek.hstack((in_arr1, in_arr2))
print ("Output horizontally stacked array:\n ", out_arr)

'''
Output:

1st Input array : 
 [1 2 3]
2nd Input array : 
 [4 5 6]
Output horizontally stacked array:
  [1 2 3 4 5 6]
  '''

# Python program explaining
# hstack() function
  
import numpy as geek
  
# input array
in_arr1 = geek.array([[ 1, 2, 3], [ -1, -2, -3]] )
print ("1st Input array : \n", in_arr1) 
  
in_arr2 = geek.array([[ 4, 5, 6], [ -4, -5, -6]] )
print ("2nd Input array : \n", in_arr2) 
  
# Stacking the two arrays horizontally
out_arr = geek.hstack((in_arr1, in_arr2))
print ("Output stacked array :\n ", out_arr)

'''
Output:

1st Input array : 
 [[ 1  2  3]
 [-1 -2 -3]]
2nd Input array : 
 [[ 4  5  6]
 [-4 -5 -6]]
Output stacked array :
  [[ 1  2  3  4  5  6]
 [-1 -2 -3 -4 -5 -6]]
 '''

# Python program explaining
# numpy.concatenate() function
  
# importing numpy as geek 
import numpy as geek
  
arr1 = geek.array([[2, 4], [6, 8]])
arr2 = geek.array([[3, 5], [7, 9]])
  
gfg = geek.concatenate((arr1, arr2), axis = 0)
  
print (gfg)

'''
Output :

[[2 4]
 [6 8]
 [3 5]
 [7 9]]
 '''


# Python program explaining
# numpy.vsplit() function
  
# importing numpy as geek 
import numpy as geek
  
arr = geek.arange(9.0).reshape(3, 3)
  
gfg = geek.vsplit(arr, 1)
  
print (gfg)

'''
Output :

[array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.],
       [ 6.,  7.,  8.]])]

'''

# Python program explaining
# numpy.hsplit() function
  
# importing numpy as geek 
import numpy as geek
  
arr = geek.arange(16.0).reshape(4, 4)
  
gfg = geek.hsplit(arr, 2)
  
print (gfg)

'''
Output :

[array([[  0.,   1.],
       [  4.,   5.],
       [  8.,   9.],
       [ 12.,  13.]]), array([[  2.,   3.],
       [  6.,   7.],
       [ 10.,  11.],
       [ 14.,  15.]])]
'''




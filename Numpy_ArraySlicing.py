import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
arr[3: ]

'''
Output:

array([4, 5, 6, 7, 8])
'''

print(arr[ : -3])
print(arr[3  :  -3])

'''
Output:

[1 2 3 4 5]
[4 5]
'''

arr = np.array([[1,2,3,4],[5,6,7,8],[8,7,6,5],[4,3,2,1]])
arr

'''
Output:

array([[1, 2, 3, 4],
       [5, 6, 7, 8],
       [8, 7, 6, 5],
       [4, 3, 2, 1]])
'''
# This is the 2D array which we will be using.
print(arr[ 3 , 1])
print()
print(arr[ 1: , 1:])
'''
Output:
3

[[6 7 8]
 [7 6 5]
 [3 2 1]]
'''

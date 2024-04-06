import numpy as np
 
# sort along the first axis
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = 0)       
print ("Along first axis : \n", arr1)       
 
 
# sort along the last axis
a = np.array([[10, 15], [12, 1]])
arr2 = np.sort(a, axis = -1)       
print ("\nAlong first axis : \n", arr2)
 
 
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = None)       
print ("\nAlong none axis : \n", arr1)


'''
Output: 

Along first axis : 
 [[10  1]
 [12 15]]

Along first axis : 
 [[10 15]
 [ 1 12]]

Along none axis : 
 [ 1 10 12 15]
 '''



arr = np.array([[7,3,8,6,4], [7,2,9,8,6],[5,4,2,3,1]])
print(np.sort(arr , axis = 0, kind = 'mergesort'))
print()
print(np.sort(arr , axis = 1, kind = 'quicksort'))
print()
print(np.sort(arr , kind = 'heapsort'))

'''
Output: 

[[5 2 2 3 1]
 [7 3 8 6 4]
 [7 4 9 8 6]]

[[3 4 6 7 8]
 [2 6 7 8 9]
 [1 2 3 4 5]]

[[3 4 6 7 8]
 [2 6 7 8 9]
 [1 2 3 4 5]]
 '''

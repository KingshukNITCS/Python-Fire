lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
  if (i > 5):
    print(i)

'''
Output
6
7
8
9
10
'''

# Now if we convert the list into an array we can do it simply in a single line.
lst = np.array([1,2,3,4,5,6,7,8,9,10])
print(lst[lst>5]) #in a single line we have done the same thing which we did previously and this time without using the for loop

# Output : [ 6  7  8  9 10]

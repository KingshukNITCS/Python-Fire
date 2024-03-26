List1= [ [1, 2, 3, 5], [4, 6, 7, 9], [8, 10, 11, 13] ]
#Accesing the rows of the list
for i in List1:
  print(i, end = ' -- ')
  
#Accessing each element of a 2D-list 
print("\n")
for i in range(len(List1)):
  for j in range(len(List1[i])):
                 print(List1[i][j], end=" , ") 



List1 = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
List1.append([5, 10, 15, 20, 25]) 
print(List1) 




List = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
List[0].extend([12, 14, 16, 18]) 
print(List)
#Output - [[2, 4, 6, 8, 10, 12, 14, 16, 18], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]



List = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
List[0].reverse()
print(List)




matrix = [
    [2, 4, 8],
    [4, 9, 6, 5],
    [6, 8, 9]
]
flattened_list = [element for row in matrix for element in row]
print(flattened_list)

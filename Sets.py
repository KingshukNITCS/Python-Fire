Set={1,2,3,4}
Set.add(6)
Set.update([4,5,6])
print(Set) # Output - {1, 2, 3, 4, 5, 6}


Set = {1,2,3, 4,5,7,8,9}
Set.remove(5)
Set.discard(3)
popped_element = Set.pop()
print(Set,f"Popped element is {popped_element}") # Output - {2, 4, 7, 8, 9} Popped element is 1


set1 = {2, 3, 4, 5, 6}
set2 = {4, 5, 7, 9, 1}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set2-set1
symmeteric_diff = set1 ^ set2
print(f"union set : {union_set}")
print(f"intersection set : {intersection_set}")
print(f"difference of sets : {difference_set}")
print(f"symmetric difference : {symmeteric_diff}")
'''
Output - union set : {1, 2, 3, 4, 5, 6, 7, 9}

intersection set : {4, 5}

difference of sets : {1, 9, 7}

symmetric difference : {1, 2, 3, 6, 7, 9}
'''

Set = {2, 3, 4, 7, 8, 0}
copy_set = Set.copy()
set_length = len(Set)
print("copy of set ", copy_set," set length ", set_length)
Set.clear()
print("Original set ", Set)
'''
Output - ('copy of set ', set([0, 2, 3, 4, 7, 8]), ' set length ', 6)

('Original set ', set([]))
'''


Set = {2, 4, 5, 7, 8}
if 5 in Set:
    print("5 is in the set")
'''
in and not in: Checks for membership in a set.
'''


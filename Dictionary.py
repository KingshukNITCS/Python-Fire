Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict = dict({1: 'Data', 2: 'Science', 3: 'Python'})
print("Dictionary with the use of dict() method: ")
print(Dict)

Dict = dict([(1, 'Data'), (2, 'Science')])
print("Dictionary with each item as a pair: ")
print(Dict)




my_dict = {'name':'Rose', 'age': 24}
print(my_dict['name'])  
print(my_dict['age'])   
print(my_dict.get('name','Unknown')) 
print(my_dict.get('city','Unknown')) #if city not there then unknown printed

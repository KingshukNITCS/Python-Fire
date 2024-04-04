'''
Exception Handling
A try except will allow you to execute code that might raise an exception and in the case of any exception or a specific one we can handle or catch the exception and execute specific code. This will allow us to continue the execution of our program even if there is an exception.

Python tries to execute the code in the try block. In this case if there is any exception raised by the code in the try block, it will be caught and the code block in the except block will be executed. After that, the code that comes after the try except will be executed.
'''

try :
  # enter the code that might cause exception
except :
  # write the exception handling code


'''
Try - Except
Try and except statements are used to catch and handle exceptions in Python. Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause.
'''
a = [2,4,5,6]
try : 
  a[5]= 20
except :
  print("index out of bound")



'''
Catching specific Exceptions
We can deal with more than one exception, that can occur from the except block. The Block of the except clause can be written to handle multiple exception by using multiple except block.
'''

a = [2,3,'abc', 5, 'geek']
try:
  a[2] = int(a[2])
  a[3] = a[3]/a[1]
except IndexError:
  print("Index out of bound")
except ValueError:
  print("the value can not be converted to Int type")
except DivideByZero:
  print("Can not divide by zero")


'''
Try-Except-Else
In addition to the try and except blocks, you can also use an else block in Python to specify code that should be executed if no exceptions are raised in the try block.
'''
a = [2, 7, 4, 3]
try: 
  c = a[2]//(4-a[3])
except:
  print("Cannot divide by zero")
else :
  print("the value of c is" , c)
  
# Output - The value of c is 4

'''
Try - Except - Finally

The try block can be followed by finally block which is always executed whether the try block passes or fails.  
'''
try:
    # Some Code.... 

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)
'''
try block contains the code that may raise an exception.

The except block(s) catch and handle specific exceptions that may occur. If no exceptions occur, the code in the else block is executed.

The else block contains code that is executed if no exceptions occur in the try block.

The finally block contains code that is always executed, whether an exception occurs or not. This block is useful for cleanup tasks or releasing resources.
'''



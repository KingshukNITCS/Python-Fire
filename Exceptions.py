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



'''
Raise Statement
When catching exceptions, it's important to consider the context and decide whether to handle the exception locally or raise a new one. The raise statement is useful when you want to propagate an exception with additional information or when you want to replace a caught exception with a more specific one. The except statement is used to
'''
def divide_numbers(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        # You can choose to re-raise the caught exception or raise a different one.
        raise ValueError("Custom error message") from e

# Example usage:
try:
    result = divide_numbers(10, 2)
    print(f"Result: {result}")
except ValueError as ve:
    print(f"Caught a ValueError: {ve}")
except ZeroDivisionError as zde:
    print(f"Caught a ZeroDivisionError: {zde}")
'''
In the above code, the divide_numbers function attempts to divide a by b. If b is zero, a ZeroDivisionError is explicitly raised with a custom error message. If any other exception occurs during the division, it catches the exception, prints an error message, and then raises a ValueError with a different custom error message.
'''

'''
Assertion in Python
Assertions are used to check whether a given logical expression is true or false. If the expression is false, the interpreter will raise an AssertionError exception, and if it's true, the program will continue executing. Assertions are typically used during development and testing to catch potential errors early.
'''
assert Expressions, message 

'''
The 'Expressions' is the conditional being tested.

message (optional) is an error message that is displayed if the assertion fails.
'''
x = 5
assert x > 0, "x should be greater than 0"

name = "John"
assert len(name) >= 3, "Name should be at least 3 characters long"

'''
assertions are useful for catching programming errors early in the development process, but they should not be used to handle runtime errors or replace proper error handling mechanisms.
'''






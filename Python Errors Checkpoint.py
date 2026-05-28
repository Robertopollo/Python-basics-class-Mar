### index error

mylist=[14, "hello", 967]
# IndexError: list index out of range
# The list `mylist` has indices 0, 1, and 2. Trying to access index 6 is out of bounds.
# To fix, access a valid index, for example, index 0:
mylist[0] # This will correctly access the first element, '14'

# ModuleNotFoundError: No module named 'Pandas'
# Module names in Python are case-sensitive. The correct names for these libraries are 'pandas' and 'numpy' (all lowercase).
import pandas
import numpy

### syntax error

# SyntaxError: invalid syntax
# The 'print' function must be all lowercase and its arguments must be enclosed in parentheses.
print("python errors")

### key error

mydictionnary={True:"hello",False:"bye", '3':"python"}
# KeyError: 'True'
# The dictionary has a boolean key `True`, not a string key `'True'`.
# To access the value, use the boolean key directly:
mydictionnary[True] # This will correctly return 'hello'

### indentation error

i=14
while i<78:
    # IndentationError: expected an indented block after 'while' statement
    # In Python, code blocks (like those in a while loop) are defined by indentation.
    # The statements inside the loop must be indented.
    print(i)
    i+=1
    
### StopIteration   

# StopIteration: This error occurs when the next() method is called on an iterator and there are no more items to be returned.
# The list has 3 elements, but next() is called 4 times. The iterator is exhausted after the third call.
# To fix this, ensure you only call next() as many times as there are elements in the iterator, or handle the StopIteration exception.
it=iter([1,2,3])
next(it)
next(it)
next(it)
# next(it) # This line causes the StopIteration error as the iterator is exhausted.

### TypeError

# TypeError: can only concatenate str (not "int") to str
# This error occurs because you are trying to add a string and an integer directly.
# Python does not automatically convert between types for concatenation with the '+' operator.
# To fix this, you need to explicitly convert the integer to a string or the string to an integer.
# Example fix: Convert the integer to a string to allow string concatenation.
'15' + str(15)

### ValueError

# ValueError: invalid literal for int() with base 10: 'python'
# This error occurs because the int() function is trying to convert a string 'python'
# which is not a valid integer representation, into an integer. The int() function
# can only convert strings that look like numbers (e.g., '123').
# To fix this, provide a string that represents a valid integer.
int('123')

### NameError

# NameError: name 'python' is not defined
# This error occurs because 'python' is not recognized as a defined variable, function, or valid statement.
# In Python, identifiers must be assigned a value before they can be used, or they must be part of a function call or keyword.
# To fix this, you can assign it to a variable, or if you intended to output the word 'python', you should print it as a string.
print('python')

### ZeroDivisionError

# ZeroDivisionError: division by zero
# This error occurs when you attempt to divide a number by zero, which is mathematically undefined.
# Python raises this error to prevent such an invalid operation.
# To fix this, ensure that the divisor (the number you are dividing by) is not zero.
x = 19 / 1 # Changed 0 to 1 to resolve the error

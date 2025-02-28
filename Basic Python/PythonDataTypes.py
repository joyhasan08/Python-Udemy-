# Python Data Types
# Python has the following data types:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# _____________________________________________________________________________________________________________________________ 

# Getting the Data Type
# You can get the data type of any object with the type() function.
# Example
# Print the data type of the variable x:
x = 5
print(type(x)) # This is an integer

# Print the data type of the variable x:
x = "Hello World"
print(type(x)) # This is a string

# Print the data type of the variable x:
x = 20.5
print(type(x)) # This is a float

# Print the data type of the variable x:
x = 1j
print(type(x)) # This is a complex number

# Print the data type of the variable x:
x = ["apple", "banana", "cherry"]
print(type(x)) # This is a list

# Print the data type of the variable x:
x = ("apple", "banana", "cherry")
print(type(x)) # This is a tuple

# Print the data type of the variable x:
x = range(6)
print(type(x))

# Print the data type of the variable x:
x = {"name" : "John", "age" : 36}
print(type(x)) # This is a dictionary

# Print the data type of the variable x:
x = {"apple", "banana", "cherry"}
print(type(x)) # This is a set

# Print the data type of the variable x:
x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # This is a frozenset

# Print the data type of the variable x:
x = True
print(type(x)) # This is a boolean

# Print the data type of the variable x:
x = b"Hello"
print(type(x)) # This is a bytes object

# Print the data type of the variable x:
x = bytearray(5)
print(type(x)) # This is a bytearray object

# Print the data type of the variable x:
x = memoryview(bytes(5)) # This is a memoryview object
print(type(x))

# _____________________________________________________________________________________________________________________________ 
# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
# Example
x = 5
y = "John"
z = 20.5 
print(x)
print(y)
print(z)

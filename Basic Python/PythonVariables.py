x = 5
y = "Hello, World!"
print(x)
print(y)
# Variables do not need to be declared with any particular type and can even change type after they have been set.


# Casting
# If you want to specify the data type of a variable, this can be done with casting.
# Example
a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0
print(a)
print(b)
print(c)


# Get the Type
# You can get the data type of a variable with the type() function.
# Example
age = 5
name = "John"
print(type(age))
print(type(name))

# Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
# Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
# Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
# Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)    
print(z)

# Output Variables
# The Python print statement is often used to output variables.
# Example
x = "awesome"
print("Python is " + x)

# You can also use the + character to add a variable to another variable:
# Example
x = "Python is "
y = "awesome"
z =  x + y
print(z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# Example
x = 5
y = "John"
print(x + y) # This will give you an error

# Right Way
x = 5
y = "John"
print(x, y)

# To fix this, you have to convert the number to a string:
# Example
x = 5
y = "John"
print(str(x) + y)
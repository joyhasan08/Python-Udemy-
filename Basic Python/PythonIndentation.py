# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.
# Python will give you an error if you skip the indentation:
# The number of spaces is up to you as a programmer, but it has to be at least one.

# Example
if 5 > 2:
print("Five is greater than two!") 
# you will get an error
# The number of spaces is up to you as a programmer, but it has to be at least one.

# Example
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!") 
        # you will get an error
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:



# Right Indentation
if 5 > 2:
  print("Five is greater than two!") 

# Right Indentation
if 5 > 2:
 print("Five is greater than two!")
 print("Five is greater than two!")

#Right Indentation
if 5 > 2:
 print("Five is greater than two!")
 if 5 > 2:
  print("Five is greater than two!")
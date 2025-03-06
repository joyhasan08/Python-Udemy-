# Python - List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # This will give you apple, banana, mango
# Explanation: The newlist contains the items in the list that have an "a" in them.
# ___________________________________________________________________________________________________________________________________________________________________
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) # This will give you apple, banana, mango
# Explanation: The example above is more readable and easier to understand than a regular for loop.
# ___________________________________________________________________________________________________________________________________________________________________
# Syntax
# newlist = [expression for item in iterable if condition == True] 
# The return value is a new list, leaving the old list unchanged.
# ___________________________________________________________________________________________________________________________________________________________________
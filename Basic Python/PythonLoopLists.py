# Python - Loop Lists
# You can loop through the list items by using a for loop:
# Example
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) # This will give you apple, banana, cherry 
#   Note: The values are not printed in the same order as they are in the list
#
# You can also loop through the list items by referring to their index number.
# Example
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) # This will give you apple, banana, cherry`
#   Note: The values are printed in the same order as they are in the list
#
# You can also use a while loop to loop through the list items:
# Example
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i]) # This will give you apple, banana, cherry
  i = i + 1 
#   Note: The values are printed in the same order as they are in the list
#
# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# Example   
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # This will give you apple, banana, cherry
#   Note: The values are not printed in the same order as they are in the list
#   
# The list comprehension method above is the shortest way to loop through a list, but it is not always the most readable way to do so.
#
# Python - Loop Lists
# There are several ways to loop through a list:
# for loop: Loop through the list items
# for loop: Loop through the index numbers
# while loop: Loop through the list items
# list comprehension: Loop through the list items
#
# ___________________________________________________________________________________________________________________________________________________________________

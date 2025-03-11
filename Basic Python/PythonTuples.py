# Python Tuples
# Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Example
thistuple = ("apple", "banana", "cherry")
print(thistuple) # This will give you ('apple', 'banana', 'cherry')
# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Example
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # This will give you banana
# Negative Indexing
# Negative indexing means starting from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
# Example
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # This will give you cherry    
# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range the return value will be a new tuple with the specified items.
# Example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # This will give you ('cherry', 'orange', 'kiwi') Note: The search will start at index 2 (included) and end at index 5 (not included).
# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:
# Example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # This will give you ('orange', 'kiwi', 'melon') Note: The search will start at index -4 (included) and end at index -1 (not included).
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Example
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant" # This will raise an error
print(thistuple)
# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
# Example
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)    # This will give you apple, banana, cherry

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
# Example
thistuple = ("apple", "banana", "cherry") 
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple") # This will give you Yes, 'apple' is in the fruits tuple
# Tuple Length
# To determine how many items a tuple has, use the len() function:
# Example
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # This will give you 3 
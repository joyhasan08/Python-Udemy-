# Python - Remove List Items
# To remove an item in a list, use the remove() method:
# Example
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # This will give you ['apple', 'cherry'] Note: The list will no longer contain the value "banana"

# You can also use the pop() method to remove an item, but this method will remove the specified index, (or the last item if the index is not specified):
# Example
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # This will give you ['apple', 'cherry'] Note: The list will no longer contain the value "banana"

# You can also use the del keyword to remove an item:
# Example
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # This will give you ['banana', 'cherry'] Note: The list will no longer contain the value "apple"

# The clear() method empties the list:
# Example
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # This will give you [] Note: The list will be empty

# The del keyword can also delete the list completely:
# Example
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) # This will raise an error because the list no longer exists Note: The list no longer exists 
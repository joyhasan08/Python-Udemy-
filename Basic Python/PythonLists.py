# Lists are used to store multiple items in a single variable.
#
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.           
#
# Lists are created using square brackets:
#   
# Example
thislist = ["apple", "banana", "cherry"]
print(thislist) # This will give you ['apple', 'banana', 'cherry']

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Example
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # This will give you banana

# Negative Indexing
# Negative indexing means starting from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
# Example
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # This will give you cherry

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range the return value will be a new list with the specified items.
# Example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # This will give you ['cherry', 'orange', 'kiwi']  Note: The search will start at index 2 (included) and end at index 5 (not included).

# Range of Negative Indexes
# Specify negative indexes to start the search from the end of the list:
# Example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # This will give you ['orange', 'kiwi', 'melon'] Note: The search will start at index -4 (included) and end at index -1 (not included).



# ___________________________________________________________________________________________________________________________________________________________________
# Change Item Value
# To change the value of a specific item, refer to the index number:
# Example
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # This will give you ['apple', 'blackcurrant', 'cherry']

# Change a Range of Item Values
# To change the value of a range of items, use the slice syntax:
# Example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # This will give you ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'melon', 'mango'] 
# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# Example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon", "pineapple"]
print(thislist) # This will give you ['apple', 'blackcurrant', 'watermelon', 'pineapple', 'orange', 'kiwi', 'melon', 'mango'] 
# Note: The length of the list will change when the number of items inserted does not match the number of items replaced. 
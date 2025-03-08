# Python - Sort Lists
# You can sort a list alphabetically by using the sort() method.
# Example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # This will give you ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
# Note: The list will be permanently changed.
# ___________________________________________________________________________________________________________________________________________________________________
# You can also sort the list in descending order by using the keyword argument reverse=True in the sort() method.
# Example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # This will give you ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
# Note: The list will be permanently changed.   
# ___________________________________________________________________________________________________________________________________________________________________
# If you want to sort a list but keep the original order, you can use the sorted() function.
# Example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(sorted(thislist)) # This will give you ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
print(thislist) # This will give you ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
# Note: The list will not be permanently changed.   
# ___________________________________________________________________________________________________________________________________________________________________
# You can also customize your sort function by using the keyword argument key = function.
# Example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
def myfunc(n):
    return len(n)
thislist.sort(key = myfunc)
print(thislist) # This will give you ['kiwi', 'banana', 'mango', 'orange', 'pineapple']
# Note: The list will be permanently changed.
# ___________________________________________________________________________________________________________________________________________________________________
# You can also customize your sort function by using the keyword argument key = lambda function.
# Example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(key = lambda x: len(x))
print(thislist) # This will give you ['kiwi', 'banana', 'mango', 'orange', 'pineapple']
# Note: The list will be permanently changed.
# ___________________________________________________________________________________________________________________________________________________________________
# Reverse Order
# If you want to reverse the order of a list, use the reverse() method.
# Example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.reverse()
print(thislist) # This will give you ['banana', 'pineapple', 'kiwi', 'mango', 'orange']
# Note: The list will be permanently changed.
# ___________________________________________________________________________________________________________________________________________________________________
# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.  
# There are ways to make a copy, one way is to use the built-in List method copy().
# Example
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # This will give you ['apple', 'banana', 'cherry']
# Note: The list will be copied.
# ___________________________________________________________________________________________________________________________________________________________________
# Another way to make a copy is to use the built-in method list().
# Example
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # This will give you ['apple', 'banana', 'cherry']
# Note: The list will be copied.    
# ___________________________________________________________________________________________________________________________________________________________________
# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
# Example
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # This will give you ['a', 'b', 'c', 1, 2, 3]
# Note: The list will be joined.
# ___________________________________________________________________________________________________________________________________________________________________
# Reverse Order
# If you want to reverse the order of a list, use the reverse() method.
# Example
thislist = ["apple", "banana", "cherry"]
thislist.reverse()
print(thislist) # This will give you ['cherry', 'banana', 'apple']
# Note: The list will be reversed.
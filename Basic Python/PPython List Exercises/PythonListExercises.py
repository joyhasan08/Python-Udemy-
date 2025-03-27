Python List Exercises
Write a Python program to sum all the items in a list. 
'''
def sum_list(items): 
    sum_numbers = 0
    for x in items: 
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))
'''
Write a Python program to multiplies all the items in a list.
'''
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))
'''
Write a Python program to get the largest number from a list.
'''
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))
'''
Write a Python program to get the smallest number from a list.
'''
def min_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(min_num_in_list([1, 2, -8, 0]))
'''
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
'''
def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr
print(match_words(['abc', 'xyz', 'aba', '1221']))
'''
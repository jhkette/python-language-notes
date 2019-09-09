# LISTS
# syntax

#List comprehension
# [__ for __ in __]
name = 'hello'
x = [char.upper() for char in name]
print(x)
print(''.join(x)) #join

cons = [c for c in 'amazing' if c not in ['a','e','i','o','u']]
print(cons) #no vowels

def remove(lst): # function that removes every other
    return [val for i, val in enumerate(lst) if i % 2 == 0]

print(remove('hello'))


nested_lists = [[1,3], [1,2], [2,3]]
# products of nested lists
product = [item * item1 for (item, item1) in nested_lists]
print(product)
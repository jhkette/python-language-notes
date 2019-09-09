# DICTIONARIES 
# 
# Itereating
#  

dictionary = {1: 'hello', 2: 'what', 3: 'hey'}

for v in dictionary.values():
    print(v)

for k in dictionary.keys():
    print(k)

for k,v in dictionary.items():
    print (k,v)


# Make a dictionary
x = dict.fromkeys('a','b')
print(x)

new_user = dict.fromkeys(['name', 'email', 'profile'], None)
print(new_user)

# dictionary comprehension
number = {1:1, 2:2, 3:3}
# this squares the values
squared = {k:v **2 for k,v in number.items()}
print(squared)



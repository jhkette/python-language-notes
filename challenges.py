# revsers string python
import string

def reverse_string(stri):
    # implement your function here
    rev = stri[::-1]
    return rev


# using reverse string
def reverse(string): 
    string = "".join(reversed(string)) 
    return string 


# remove every other in a list
def remove_every_other(lst):
    return [val for i, val in enumerate(lst) if i % 2 == 0]

#vowel count
def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


def find_factors1(num):
    # x=num
    final = []
    numbers = list(range(1, num +1))
    # print(numbers)
    for number in numbers:
        # print(num)
        # print(number)
        if num % number == 0:
            final.append(number)
    return final


# write a function called find factors which accepts a number and returns a list of
#  all the are divsible , starting from 1 going uo to that number
'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''
def find_factors(num):

    return [number for number in list(range(1,num+1)) if num % number == 0]

print(find_factors(12))


#write a function called repeat, which accpets  a string and a number and returns a new string
#with the string passed to the function repeatd the number of times
'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''

def repeat(string, num):
    final = string
    if num == 0:
        return ''
    for n in range(1,num):
        final += string
    return final

print(repeat('hello', 2))


def truncate(string, num):
    if len(string) < num or 2 > num:
        return string
    new = string[:-num]
    new3=new + '...'
    return new3
print(truncate('Hello World', 6))

def two_list_dictionary(list1, list2):
    if len(list1) > len(list2):
        for i in range(len(list1) -len(list2)):
            list2.append(None)     
    return dict(zip(list1, list2))

# print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))

def same_frequency(num1, num2):
    x = dict.fromkeys(str(num1), None)
    y = dict.fromkeys(str(num2), None)

    return x, y

# print(same_frequency(551122,221515))

def find_the_duplicate(nums):
    x = dict.fromkeys(nums, 0)
    for i in nums:
        x[i] +=1
    for k,v in x.items():
        if v > 1:
            return k
    return None
print(find_the_duplicate([2,1,3,4,3]))
    

# def thee_odd_numbers(nums):
# sum pairs solution - find pairs that match sum in an array

def sum_pairs(nums, target):
    already_visited = set() # a set of numbers
    for i in nums: # i in nums
        difference = target - i # find difference
        if difference in already_visited: # if difference in visited
            return [str(difference) +'this is the difference', str(i)] # 
        already_visited.add(i) # add i to already visited
    return []




# sum_pairs([11,20,4,2,1,5], 100) 
print(sum_pairs([4,2,10,5,1], 6)) # [4,2]


    
        




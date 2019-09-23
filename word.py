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

# Find factors






def repeat(string, num):
    final = string
    if num == 0:
        return ''
    for n in range(1,num):
        final += string
    return final

print(repeat('hello', 2))

x = 'hellothere'
y = x[:-3]
print(y)
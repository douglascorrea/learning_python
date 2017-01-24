"""
Implementing it withou use string function to split it into a list of numbers
"""
s = input('Input a list of numbers separated by comma: ')
acc = '0'
total = 0
for n in s:
    if n != ',':
        acc = acc + n
    else:
        total = total + float(acc)
        acc = '0'
total = total + float(acc)
print(total)

from copy import deepcopy

# d2 = d1 = {'a': 1, 'b': 2, 'c': 3}
d1 = {'a': 1, 'b': 2, 'c': 3, 'f': [6, 7, 8]}
d2 = deepcopy(d1)

print('1.', '-' * 40)
print(d1)
print(d2)

d1['d'] = 4
d2['e'] = 5
print('2.', '-' * 40)
print(d1)
print(d2)

d1['f'].append(9)
d2['f'].append(10)
print('3.', '-' * 40)
print(d1)
print(d2)

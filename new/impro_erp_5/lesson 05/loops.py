lst = [1, 2, 3, 4]

for el in lst:
    print(el, end=', ')

print('end!')
print('-' * 40)

for i in range(10):
    print(i, end=', ')
print()
print('-' * 40)

for i in range(1, 10):
    print(i, end=', ')

print()
print('-' * 40)

for i in range(1, 10, 2):
    print(i, end=', ')

print()
print('-' * 40)

for i in range(2, 20, 2):
    print(i, end=', ')

print()
print('-' * 40)

for i in range(10, 0, -1):
    print(i, end=', ')

print()
print('-' * 40)

lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(lst2)
for i in range(n):
    print(i, end=', ')

print()
print('-' * 40)

for i in range(n):
    print(lst2[i], end=', ')

print()
print('-' * 40)

d1 = {'a': 1, 'b': 2, 'c': 3}
for key in d1:
    print(key)
print()
print('-' * 40)
for key in d1:
    print(d1[key])

print()
print('-' * 40)
for key in d1.keys():
    print(key)

print()
print('-' * 40)
for val in d1.values():
    print(val)

print()
print('-' * 40)
for key, val in d1.items():
    print(key, val, sep=':')

print()
print('-' * 40)

i = 1
while i <= 10:
    print(i, end=', ')
    i += 1

print()
print('-' * 40)

i = 0
while i >= -10:
    print(i, end=', ')
    i = i - 1

print()
print('-' * 40)

lst3 = [10, 7, 4, 8, 2, 8]
s = 0
for el in lst3:
    s += el
print(s)

print('-' * 40)

lst4 = [10, 3, 1, 7, 4, 8, 2, 8]
s1 = 0
s2 = 0
for el in lst4:
    if el % 2 == 0:
        s2 += el
    else:
        s1 += el
print(s1, s2)
print('-' * 40)

s1 = 0
s2 = 0
for el in lst4:
    if el % 2:
        s1 += el
    else:
        s2 += el
print(s1, s2)
print('-' * 40)

x = int(input('Enter x: '))

for i in range(x):
    print(i, end=', ')

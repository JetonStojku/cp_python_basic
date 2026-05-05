d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d)
d['e'] = 5
print(d)
d['a'] = 8
print(d)
print(d['a'])
print(d.get('a'))
print(d.get('z', 0))

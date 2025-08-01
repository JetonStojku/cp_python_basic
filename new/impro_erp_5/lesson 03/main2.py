d = {
    'a': 1,
    'b': 2,
    3: 'c',
}
print(d)
print(d['a'])
print(d[3])

d['b'] = 7
print(d['b'])
d['c'] = 20
print(d)

d1 = {
    'a': 127,
    'key2': 20,
    'key3': [1, 2, 3, 74],
    'key4': {'a1': [1, 2, 3, {'b1': 7, 'b2': [2, 3, 4, 8]}]}
}
print(d1['a'])
print(d1['key3'])
print(d1['key3'][3])
print(d1['key4']['a1'][3]['b2'])
print(d1['key4']['a1'][3]['b2'][3])

d = {'key1': 1, 'key2': 2, 'key3': 3}
print(d)
print(d.keys())
print(d.values())
print(d.items())

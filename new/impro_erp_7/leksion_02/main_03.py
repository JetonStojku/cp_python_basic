d = {
    'a': 1,
    'b': 2,
    'c': 3,
}
print(d)
print(d['a'])

d1 = {
    2: "c",
    0: "a",
    1: "b",
}

print(d1[0])
print(d1[1])
print(d1[2])

d = {
    'a': 1,
    'b': 'Hello',
    'c': [2, 3, 4],
    'd': {'e': [5, 6, {'f': [7, 8]}]}
}
print(d['d']['e'][2]['f'][1])

d = {
    'a': 1,
    'b': 'Hello',
    'b': 2,
}
print(d)
d['c'] = 3
print(d)
d['a'] = 0
print(d)
# print(d['g'])
print(d.get('g', 0))
print(d.keys())
print(d.values())
print(d.items())

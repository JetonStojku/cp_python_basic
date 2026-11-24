d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

for key in d:
    print(key)

for key in d:
    print(d[key])

for key in d.keys():
    print(key)

for val in d.values():
    print(val)

for key, val in d.items():
    print(key, val)

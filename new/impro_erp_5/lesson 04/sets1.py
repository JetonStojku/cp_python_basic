dcs = {1, 'a', 4, 3, 2, 1, 2, 4, 'b'}
print(dcs)

lst = [1, 'a', 4, 3, 2, 1, 2, 4, 'b']
print(lst)
lst = list(set(lst))
print(lst)

dcs.add(5)
print(dcs)
dcs.add('a')
print(dcs)

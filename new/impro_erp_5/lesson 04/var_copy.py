from copy import deepcopy

# lst2 = lst1 = [1, 2, 3, 4]
lst1 = [1, 2, 3, 4]
lst2 = lst1
print(lst1)
print(lst2)
print('-' * 40)

lst1.append(5)
lst2.append(6)

print(lst1)
print(lst2)
print('-' * 40)
print('=' * 80)
lst3 = [1, 2, 3, 4, {'a': 5}]
lst4 = lst3.copy()
print(lst3)
print(lst4)
print('-' * 40)
lst3.append(5)
lst4.append(6)
print(lst3)
print(lst4)
print('-' * 40)
lst3[4]['b'] = 7
lst4[4]['c'] = 8
print(lst3)
print(lst4)
print('-' * 40)
print('=' * 80)
lst5 = [1, 2, 3, 4, {'a': 5}]
lst6 = deepcopy(lst5)
print(lst5)
print(lst6)
print('-' * 40)
lst5.append(5)
lst6.append(6)
print(lst5)
print(lst6)
print('-' * 40)
lst5[4]['b'] = 7
lst6[4]['c'] = 8
print(lst5)
print(lst6)
print('-' * 40)

print('=' * 80)
lst = [1, 2, 3, 4, {'a': 5}]
d = lst[4]
print(lst)
print(d)
print('-' * 40)
d['e'] = 6
print(d)
print(lst)
print('-' * 40)

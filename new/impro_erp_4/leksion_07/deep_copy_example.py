from copy import deepcopy

lst1 = [1, 2, 3, 4, {'a': 5, 'b': 6}]
lst2 = lst1
lst3 = lst1.copy()
lst4 = deepcopy(lst1)
print('--' * 20)
print(lst1)
print(lst2)
print(lst3)
print(lst4)

lst1.append(7)
lst2.append(8)
lst3.append(9)
lst4.append(10)
print('--' * 20)
print(lst1)
print(lst2)
print(lst3)
print(lst4)

lst1[4]['c'] = 11
lst2[4]['d'] = 12
lst3[4]['e'] = 13
lst4[4]['f'] = 14
print('--' * 20)
print(lst1)
print(lst2)
print(lst3)
print(lst4)

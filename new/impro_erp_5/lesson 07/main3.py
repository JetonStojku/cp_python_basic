def even(a):
    return a % 2 == 0
    # if a % 2 == 0:
    #     return True
    # else:
    #     return False


lst = [7, 4, 3, 2, 8, 10]
lst1 = []

for el in lst:
    if even(el):
        lst1.append(el)

print(lst1)
print('-' * 40)

lst2 = list(filter(even, lst))
print(lst2)
print('-' * 40)

lst3 = list(filter(lambda a: a % 2 == 0, lst))
print(lst3)

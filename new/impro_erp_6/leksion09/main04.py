def add(a, b=None):
    if b is None:
        b = []
    if 0 < a <= 10:
        b.append(a)
    return b


x = 7
lst1 = add(x)
print(lst1)

y = 5
lst2 = add(y)
print(lst2)

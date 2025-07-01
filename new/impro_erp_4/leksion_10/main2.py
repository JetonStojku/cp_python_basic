def add(a, b):
    return a + b


s = add(4, 6)
print(s)

lst = [4, 6]
s = add(*lst)
print(s)

s = add(b=6, a=4)
print(s)

d = {'a': 4, 'b': 6}
s = add(d['a'], d['b'])
print(s)

s = add(**d)
print(s)

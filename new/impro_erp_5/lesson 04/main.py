lst = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
print(t, lst)
print(t[0], lst[0])
print(t[1:3], lst[1:3])

lst[2] = 8
lst.append(6)
print(lst)

d = {(1, 2, 3): 6}
print(d[(1, 2, 3)])

t = (1, 2, 3, 4, 5, 6)
print(t)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
print(lst[1])
print(lst[-1])
print(lst[1:4])
print(lst[1:5:2])
print(lst[3:0:-1])
print(lst[::-1])
print(lst[1:3])
print(lst[1:2])
print(lst[1])
print(lst[1:1])
print(lst[1:0])

lst1 = [1, 2, 'a']
lst2 = ['b', 'c', 3]
lst = lst1 + lst2
print(lst)

lst3 = lst1 * 2
print(lst3)
lst1.append(4)
print(lst1)
lst2.pop()
print(lst2)
lst1.pop(0)
print(lst1)
lst1.remove('a')
print(lst1)

lst4 = [7, 3, 2, 6, 9, 8, 4]
print(lst4)
lst4.reverse()
print(lst4)
lst4.sort()
print(lst4)

lst5 = [2, 7, 1, 5, 4]
print(lst5)
lst6 = sorted(lst5)
print(lst6)
print(lst5)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
l = [l1, l2, l3]
print(l)
l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(l)
print(l[0])
print(l[0][1])

l = [1, 2, 3, [4, 5, 6], [7, [8, [9]]]]
print(l[1])
print(l[3])
print(l[4])
print(l[4][1])
print(l[4][1][1])
print(l[4][1][1][0])

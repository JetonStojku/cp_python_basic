""" U1 """
"""
a) printoni numrin 9 nga lista
b) printoni listen [6, 2, 4, [7]]
c) printoni numrin 6 nga lista
d) printoni numrin 7 nga lista
e) printoni numrin 8 nga lista
f) printoni listen [6, 2, 4]
e rendisni listen [6, 2, 4] -> [2, 4, 6]
"""

lst = [1, 9, 3, 0, 5, [6, 2, 4, [7],], 8]
print(lst[1])
print(lst[5])
print(lst[5][0])
print(lst[5][3][0])
print(lst[6])
print(lst[5][:3])
print(sorted(lst[5][:3]))
lst1 = lst[5][:3]
lst1.sort()
print(lst1)

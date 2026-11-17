lst = [1, 2, "Hello", 2.4]
print(lst)

lst = [1, 2, 3, 4, 5, 6]
print(lst[2])
print(lst[-1])
print(lst[1:4])
print(lst[1:5:2])
print(lst[3:0:-1])
print(lst[::2])
print(lst[::-1])
print(lst[1:1])
print(lst[1:2])
print(lst[1])

lst = [1, 2, 3, [4, 5, 6]]
print(lst[3][1])

lst = [1, 2, 3,
       [4, 5, 6, [7, 8, [9, 10, [11, 12, [13, 14, [15, 16]]]]]],
       ]
print(lst[3][3][2][2][2][2][1])

matrix = [
    [1, 2, 3, ],
    [4, 5, 6, ],
    [7, 8, 9],
]
print(matrix[1][2])

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst = lst1 + lst2
print(lst)

lst2 = lst1 * 3
print(lst2)

matrix = [[0] * 5] * 5
print(matrix)

""" U3 """
"""
a) ndërtoni një program i cili merr nga përdoruesi
madhësinë e matricës që do japë n, m.
b) Pastaj kërkohet që useri të japë vlerat për
këtë matricë.
c) printoni matricën në formën natyrale

[[1, 2, 3], [4, 5, 6]]

print:
1 2 3
4 5 6

"""

n = int(input("Jep n: "))
m = int(input("Jep m: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        x = float(input('Jep x: '))
        row.append(x)
    matrix.append(row)

print('-' * 40)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
print('-' * 40)
for row in matrix:
    for el in row:
        print(el, end=' ')
    print()

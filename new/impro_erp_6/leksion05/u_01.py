""" U1 """
"""
Ndërtoni një program i cili printon nga një listë vetëm elementët
çift të tij.
"""

lst = [5, 10, 3, 1, 4, 8, 6, 6]

for el in lst:
    if el % 2 == 0:
        print(el)

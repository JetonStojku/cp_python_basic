""" U1 """
"""
Ndërtoni një funksion i cili merr si parametra 2 lista dhe kthen
një listë me elemente shumën e dy elementëve të të njëjstit indeks
në dy listat e tjera. Nëse listat nuk kanë gjatësi të njejtë 
kthen një listë boshe.
shembull 1:
lst1 = [1, 2, 3, 4]
lst2 =  [7, 1, 4, 10]
resultati: lst = [8, 3, 7, 14]

shembull 2:
lst1 = [1, 2, 3, 4]
lst2 =  [7, 1]
resultati: lst = []
"""


def shum(lst1, lst2):
    if len(lst1) != len(lst2):
        return []
    n = len(lst1)
    lst = []
    for i in range(n):
        lst.append(lst1[i] + lst2[i])
    return lst

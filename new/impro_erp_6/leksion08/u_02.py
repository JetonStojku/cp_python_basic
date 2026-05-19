""" U2 """
"""
Ndërtoni një funksion i cili merr si parametra 2 lista dhe kthen
një listë me elemente shumën e dy elementëve të të njëjstit indeks
në dy listat deri në elementët e listës më e shkurtër.
shembull 1:
lst1 = [1, 2, 3, 4]
lst2 =  [7, 1, 4, 10]
resultati: lst = [8, 3, 7, 14]

shembull 2:
lst1 =  [7, 1]
lst2 = [1, 2, 3, 4]
resultati: lst = [8, 3]
"""


def sum_list(lst1, lst2):
    lst = []
    if len(lst1) < len(lst2):
        n = len(lst1)
    else:
        n = len(lst2)

    for i in range(n):
        lst.append(lst1[i] + lst2[i])
    return lst


l1 = [1, 2, 3, 4]
l2 = [7, 1, 4, 10]
l3 = [1, 2, 3, 4]
l4 = [7, 1]
print(sum_list(l1, l2))
print(sum_list(l4, l3))

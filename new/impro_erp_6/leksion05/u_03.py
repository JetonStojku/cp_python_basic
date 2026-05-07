""" U3 """
"""
Ndërtoni një funksion i cili kthen një listë me numra
integer të marrë nga përdoruesi dhe merr si parameter
sa elementë do ketë lista.
"""


def create_list(n):
    lst = []
    print('Jep elementët e listës')
    for i in range(n):
        x = int(input())
        lst.append(x)
    return lst


l1 = create_list(5)
l2 = create_list(5)
print('l1 = ', l1)
print('l2 = ', l2)

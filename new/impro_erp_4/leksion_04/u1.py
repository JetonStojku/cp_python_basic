""" u1 """
"""
Ndërtoni një funksion i cili merr nga përdoruesi numnin n
dhe kthen shumën e të gjithë numrave nga 1 në n
shembull:
n = 6
përgjigja: shuma = 1 + 2 + 3 + 4 + 5 + 6 = 21
"""


def sum_number(n):
    s = 0
    i = 0
    while i < n:
        i += 1
        s += i
    return s


print(sum_number(6))

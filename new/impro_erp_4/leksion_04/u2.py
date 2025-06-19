""" u2 """
"""
Ndërtoni një funksion i cili merr nga përdoruesi
një numër n dhe gjen faktorialin e tij.
n = 5
5*4*3*2*1=120
"""


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


print(factorial(5))

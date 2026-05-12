""" U03 """
"""
Ndërtoni një funksion i cili merr nga përdoruesi një numër n
dhe printon një trekëndësh me yje si në shembull.
print nuk duhet të printojë më shumë se një karakter.
shembull: n = 4
përgjigja:
*
**
***
****
"""


def print_trekendesh(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        print()


print_trekendesh(5)

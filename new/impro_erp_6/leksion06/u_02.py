""" U02 """
"""
Ndërtoni një funksion i cili merr nga përdoruesi një numër n
dhe printon një katror me yje. print nuk duhet të printojë
më shumë se një karakter.
shembull: n = 4
përgjigja:
****
****
****
****
"""


def print_katror(n):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()


def print_katror2(n):
    print(f'{'*' * n}\n' * n)


print_katror2(8)

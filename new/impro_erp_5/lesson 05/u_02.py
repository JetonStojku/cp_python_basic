""" U2 """
"""
Ndertoni një program i cili merr nga përdoruesi
një numër n dhe printon një katror me n*n yje
"""

n = int(input('Enter n: '))
for i in range(n):
    for j in range(n):
        print(end='*')
    print()

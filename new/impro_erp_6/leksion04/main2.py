""" u1 """
"""
Ndërtoni një program i cili merr nga përdoruesi një numër
dhe printon çift nëse numri është çift dhe tek nëse është
tek.
"""

a = int(input("Enter a number: "))

if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')
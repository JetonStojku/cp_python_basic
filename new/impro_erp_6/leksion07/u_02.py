""" U02 """
"""
Gjeni nëse një numër është palindrom ose jo
"""


def palindrom(x):
    s = ''
    while x > 0:
        s = s + str(x % 10)
        x = x // 10
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return 'Jo palindrom'
    return 'Palindrom'


print(palindrom(11001))

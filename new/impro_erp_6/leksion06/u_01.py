""" U01 """
"""
Ndërtoni një funlsion i cili kthen elementin më të madh në një dictionary
"""


def find_max(dct):
    max = -99999
    for el in dct.values():
        if max < el:
            max = el
    return max


d = {'a': 1, 'b': 20, 'c': 3}
print(find_max(d))

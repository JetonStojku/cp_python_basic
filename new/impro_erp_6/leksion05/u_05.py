""" U5 """
"""
Ndërtoni një funksion i cili merr si parametër
një listë dhe kthen shumën e numrave çift të tij.
"""


def sum_list_even(lst):
    sum = 0
    for x in lst:
        if x % 2 == 0:
            sum += x
    return sum


l = [4, 6, 1, 1, 10, 5, 7]
s = sum_list_even(l)
print(s)

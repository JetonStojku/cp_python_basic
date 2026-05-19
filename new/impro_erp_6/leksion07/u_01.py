""" U01 """
"""
Ndërton një funksuion i cili numëron numrat pozitiv,
negativ, zero, nga numrat e dhënë nga nëj përdurues.
"""


def count_numbers(n):
    print("Enter numbers")
    t = [0, 0, 0]
    for i in range(n):
        x = float(input())
        if x < 0:
            t[0] += 1
        elif x == 0:
            t[1] += 1
        else:
            t[2] += 1
    return t


print(count_numbers(5))

"""U2"""
"""
Ndertoni nje funksion i cili merr nga perdoruesi
nje numer n dhe kthen shumen e te gjithe numrave
nga 1 deri ne n.
shembull:
n = 5
s = 1 + 2 + 3 + 4 + 5 = 15
"""


def sum(n: int) -> int:
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


print(sum(5))

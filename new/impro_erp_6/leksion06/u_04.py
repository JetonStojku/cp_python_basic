""" U04 """
"""
Ndërtoni një  funksion i cili merr nga perdoruesi
orën, minutat, sekondat dhe ndërton një countdown
duke printuar të gjitha sekondat deri te 0:0:0

shembull: 2h 12min 14sec
përgjigja:
2:12:14
2:12:13
2:12:12
.....
2:12:0
2:11:59
2:11:58
.....
2:0:0
1:59:59
.....
0:0:0
"""


def countdown(h, m, s):
    while h >= 0:
        while m >= 0:
            while s >= 0:
                print(h, m, s)
                s -= 1
            s = 59
            m -= 1
        m = 59
        h -= 1


countdown(2, 12, 14)

""" u2 """
"""
Ndërtoni një program i cili merr nga përdoruesi një numër
dhe printon çift tik nëse numri plotëpjestohet me 3,
tok nëse plotëpjestohet me 5 dhe tiktok nëse plotëpjestohet
me 3 dhe 5.
"""

a = int(input('a = '))
if a % 3 == 0 and a % 5 == 0:
    print('tiktok')
elif a % 5 == 0:
    print('tok')
elif a % 3 == 0:
    print('tik')

# if a % 3 == 0:
#     print('tik', end='')
# if a % 5 == 0:
#     print('tok')

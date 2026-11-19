"""U01"""
"""
Ndertoni nje program i cili merr nga perdoruesi nje
numer dhe printon tik nese numri plotepjestohet
me 5, tok nese plotepjestohet me 7 dhe
tiktok nese plotepjestohet me 5 dhe 7
"""

x = 5

# if x % 5 == 0 and x % 7 == 0:
#     print("tiktok")
# elif x % 5 == 0:
#     print("tik")
# elif x % 7 == 0:
#     print("tok")
#
# if x % 5 == 0:
#     if x % 7 == 0:
#         print("tiktok")
#     else:
#         print("tik")
# elif x % 7 == 0:
#     print("tok")
#
# if x % 5 == 0:
#     if x % 7 == 0:
#         print("tiktok")
#     else:
#         print("tik")
# else:
#     if x % 7 == 0:
#         print("tok")

if x % 5 == 0:
    print("tik", end='')
if x % 7 == 0:
    print("tok")

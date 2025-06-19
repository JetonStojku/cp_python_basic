""" u3 """
"""
Ndërtoni një funksion i cili merr një listë si
parametër dhe gjen shumën e numrave tek dhe
shumën e numrave çift veç e veç dhe kthen
një tuple ku këto 2 shuma

l = [1, 2, 3, 4, 5]
përgjigja: (6, 9)

"""


def shuma_tek_cift(l):
    shuma_tek = 0
    shuma_cift = 0

    for el in l:
        if el % 2 == 0:
            shuma_cift += el
        else:
            shuma_tek += el

    return shuma_cift, shuma_tek


lst = [1, 2, 3, 4, 5]
print(shuma_tek_cift(lst))

""" u5 """
"""
ndërtoni një funksion i cili merr si parametër
një listë me tuple. tuple ka të ruajtur në
index 0 sasinë e produkteve të shitur kurse në
index 1 cmimin e tyre.
funksioni duhet të llogarisi shumën totale të
fituar nga të gjitha produktet.
l = [(2, 20), (5, 100), (7, 4)]
përgjigja: 2*20+5*100+7*4=40+500+28=568
"""


def llogarit_fitimin(l):
    fitim = 0

    for sasi, cmimi in l:
        fitim += sasi * cmimi
    return fitim


lst = [(2, 20), (5, 100), (7, 4)]
print(llogarit_fitimin(lst))

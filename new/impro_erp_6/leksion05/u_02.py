""" U2 """
"""
Ndërtoni një program i cili krijon një listë me numra
integer të dhëna nga përdoruesi. Përdoruesi si fillim
do të jap gjatësinë e listës, pastaj vlerat e saj.
"""
n = int(input("Jep sa numra do kete lista: "))
lst = []
print('Jep elementët e listës')
for i in range(n):
    x = int(input())
    lst.append(x)

print(lst)

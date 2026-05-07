""" U4 """
"""
Ndërtoni një funksion i cili krijon një listë me numra
të dhëna nga përdoruesi. Përdoruesi duhet të shtypi
`exit` që të përfundojë së dhëni numra për listën.
"""


def create_list():
    lst = []
    print("Enter list values")
    while True:
        x = input()
        if x == 'exit':
            break
        x = int(x)
        lst.append(x)
    return lst


l = create_list()
print(l)

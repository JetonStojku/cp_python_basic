blerje = shitje = {}
lst = [-3, -4, 10, 25]

blerje['janar'] = 0
shitje['janar'] = 0
for el in lst:
    if el < 0:
        blerje['janar'] += el
    else:
        shitje['janar'] += el

print(blerje, shitje)

"""U1"""
"""
Ne nje liste jane ruajtur tuple me 2 element ku vlera
e parer percakton bazen kurse vlera e dyte fuqine.
a) ndertoni nje program i cili printon numrin e ngritur ne fuqi
b) llogarit shumen e te gjithe ketyre numrave
"""

lst = [(2, 4), (5, 2), (3, 0), (7, 6)]

for t in lst:
    print(t[0] ** t[1])

s = 0
for t in lst:
    s += t[0] ** t[1]

print(f"Sum = {s}")

for base, power in lst:
    print(base ** power)

s = 0
for base, power in lst:
    s += base ** power

print(f"Sum = {s}")

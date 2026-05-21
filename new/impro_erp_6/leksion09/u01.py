""" U1 """
"""
Ndërtoni një klasë të tipit faturë. Në të do të ruhen
dt, nr fature, kamarieri, nje list me totalin e cdo
produkti të marrë. Ndërrtoni një metodë që kthen
totalin e faturës
"""


class Fatur:
    def __init__(self, nr, dt, kamarieri, produktet):
        self.nr = nr
        self.dt = dt
        self.kamarieri = kamarieri
        self.produktet = produktet

    def total(self):
        s = 0
        for x in self.produktet:
            s += x
        return s


f1 = Fatur(10, '21.05.2026', 'Filan', [50, 60])
print(f1.total())

"""
Ndërtoni një klasë të tipit punonjës i cili
ka parametrat emër, mbiemër, vite_pune, pagë
Ndërtoni një metodë i cili rrit me 1 vitet
e punës së punonjësit.
Ndërtoni një metodë e cila llogarit pagën
plus një bonus (parametër i funksionit)
që duhet ti jepet punonjësit
"""


class Punonjes:
    def __init__(self, emer, mbiemer, vite_pune, page):
        self.emer = emer
        self.mbiemer = mbiemer
        self.vite_pune = vite_pune
        self.page = page

    def shto_vitet_punes(self):
        self.vite_pune += 1

    def llogarit_page_totale(self, bonus):
        return self.page + bonus


x = Punonjes('Jeton', 'Stojku', 2, 30000)
print('Para', x.emer, x.vite_pune, x.page)
x.shto_vitet_punes()
paga_x = x.llogarit_page_totale(-5000)
print('Paga:', paga_x)
print('Pas', x.emer, x.vite_pune, x.page)

""" U04 """
"""
Ndëtoni një klasë e cila do ruaj objekte të tipit laptop.
Një laptop do ketë atributet, marka, modeli, ram, hdd
cmimi, ulja në përqindje. Gjithashtu do ketë dhe një
metodë e cila do të kthej cmimin pas uljes.
"""


class Laptop:
    def __init__(self, mark, model, ram, hdd, price, discount=0):
        self.mark = mark
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.price = price
        self.discount = discount

    def get_price(self):
        return self.price * (1 - self.discount)


l1 = Laptop('HP', 'EliteBook', 16, 512, 700)
print(l1.get_price())
l1.discount = 0.1
print(l1.get_price())

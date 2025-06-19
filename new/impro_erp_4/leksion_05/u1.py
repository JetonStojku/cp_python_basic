""" u1 """
"""
Ndërtoni një klase të tipit Laptop ku të ruaj parametrat
e një laptopi si: Marka, Modeli, Ram, HDD, CPU, Monitor
Kur obljekti i tipi laptop të printohet duhet të
printohet marka - modeli
"""


class Laptop:
    def __init__(self, marka, modeli, ram, hdd, cpu, monitor, cmimi):
        self.marka = marka
        self.modeli = modeli
        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu
        self.monitor = monitor
        self.cmimi = cmimi

    def sknto_20(self):
        return self.cmimi * 0.8

    def skonto_40(self):
        return self.cmimi * 0.6

    def __str__(self):
        return f'{self.marka} - {self.modeli}'


laptop_1 = Laptop('Dell', 'XPS 15', 16, 512, 'Intel Core i7', '15.6"', 1499)

print(laptop_1, laptop_1.cmimi)
print(f"Oferta 20%: {laptop_1.sknto_20()}")
print(f"Oferta 40%: {laptop_1.skonto_40()}")

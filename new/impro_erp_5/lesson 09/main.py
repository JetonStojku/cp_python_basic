class Laptop:
    def __init__(self, brand, ram, hdd):
        self.brand = brand
        self.ram = ram
        self.hdd = hdd

    def shut_down(self):
        print('Goodbye!')

    def __str__(self):
        return f'{self.brand}: {self.ram}, {self.hdd}'


a = Laptop('hp', 16, 512)
print(a.brand, a.ram, a.hdd)
a.shut_down()
print(a)

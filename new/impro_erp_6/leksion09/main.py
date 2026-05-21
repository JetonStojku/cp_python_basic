class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


a = Animal()
a.whoAmI()
a.eat()
print('-' * 40)
d = Dog()
d.whoAmI()
d.eat()
d.bark()

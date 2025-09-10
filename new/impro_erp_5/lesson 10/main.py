from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


def no_of_sides(obj: Polygon):
    obj.noofsides()


# Driver code
r = Triangle()
k = Quadrilateral()
p = Pentagon()
h = Hexagon()
no_of_sides(r)
no_of_sides(k)
no_of_sides(p)
no_of_sides(h)
print('-' * 40)
lst = [Triangle(), Quadrilateral(), Pentagon(), Hexagon()]
for pol in lst:
    no_of_sides(pol)

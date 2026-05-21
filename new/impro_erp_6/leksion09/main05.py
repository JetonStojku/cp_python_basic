from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def no_of_sides(self):
        print("I have 4 sides")


# Driver code
r = Triangle()
r.no_of_sides()

r = Quadrilateral()
r.no_of_sides()

r = Pentagon()
r.no_of_sides()

k = Hexagon()
k.no_of_sides()

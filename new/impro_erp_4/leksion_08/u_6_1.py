""" u 6.1- 6.2 """
from abc import ABC, abstractmethod

"""
**Exercise 1: Abstract Class**
Create an abstract class called `Shape` with an abstract method `area()`. Create two subclasses, `Circle` and `Rectangle`, that inherit from the `Shape` class. Implement the `area()` method in each subclass.
"""


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


def calculate_area(shape: Shape):
    return shape.area()


d = Rectangle(8, 5)
r = Circle(3)
sip_d = calculate_area(d)
sip_r = calculate_area(r)
if sip_d > sip_r:
    print(f'Rectangle: {sip_d}')
else:
    print(f'Circle: {sip_r}')

""" u 6.5 """
from abc import ABC, abstractmethod

"""
**Exercise 5: Abstract Class Inheritance**
Create an abstract class `Vehicle` with abstract methods `start()` and `stop()`. Implement two subclasses, `Car` and `Motorcycle`, inheriting from `Vehicle`. Provide implementations for the abstract methods.
"""


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...


class Car(Vehicle):
    def start(self):
        print('Car started!')

    def stop(self):
        print('Car stop!')


class Motorcycle(Vehicle):
    def start(self):
        print('Motorcycle started!')

    def stop(self):
        print('Motorcycle stop!')


c = Car()
m = Motorcycle()

c.start()
m.start()
c.stop()
m.stop()

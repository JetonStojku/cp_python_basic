from dataclasses import dataclass


@dataclass
class Person:
    name: str
    citizenship: str
    worth: int


x = Person('Tst', 'USA', 100)
print(x)

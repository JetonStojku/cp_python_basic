""" u2 """
import json

"""
Në një json ruhen të dhënat e studentëve të një universiteti.
a) Ndërtoni një klasë e cila do të ruaj të dhënat e këtyre
    studentëve
b) Ndërtoni një funksion i cili kthen të dhënat e këtij json.
c) Ndërtoni një funksion i cili kthen një listë me
    studentë nga json i dhënë
d) Ndërtoni një metodë për studentët që kthen
    mesataren e tij
e) Gjeni studentin më të mirë
f) Gjeni kush prej gjinive ka mesatare më të lartë
"""


class Student:
    def __init__(self, first_name, last_name, age, score, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.score = score
        self.gender = gender

    def avg(self):
        return sum(self.score) / len(self.score)

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.avg()}'


def import_json(path: str) -> list[dict]:
    with open(f'data/{path}.json', 'r') as f:
        persons = json.load(f)
        return persons


def create_students_list(students: list[dict]) -> list[Student]:
    students_list = []
    for student in students:
        s = Student(**student)
        students_list.append(s)
    return students_list

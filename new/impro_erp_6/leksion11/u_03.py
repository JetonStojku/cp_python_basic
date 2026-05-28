""" U3 """
import json
from dataclasses import dataclass

"""
Në student.json janë ruajtur informacionet e studentëve.
1. Ndërtoni një klasë e cila të ruaj informacionet e këtyre
    studentëve
2. Ndërtoni një funksion i cili importon të dhënat nga file
    json dhe krijon një listë me student
3. Ndërtoni një funksion që kthen studentin më të mirë.
4. Gjeni Kush ka mesatare më të lartë femra/meshkuj
"""


@dataclass
class Student:
    country: str
    first_name: str
    last_name: str
    age: int
    grade: int
    gender: str


def import_student(file_name: str) -> list[Student]:
    with open(file_name) as f:
        students_json = json.load(f)

    students = []
    for student in students_json:
        # s = Student(student['country'], student['first_name'], student['last_name'], student['age'], student['grade'], student['gender'])
        s = Student(**student)
        students.append(s)

    return students


if __name__ == '__main__':
    st = import_student('data/student.json')
    print(st)

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


def find_best_student(students: list[Student]) -> Student:
    best_student = students[0]
    for s in students:
        if s.grade >= best_student.grade:
            best_student = s
    return best_student


# def find_best_student(students: list[Student]) -> Student:
#     best_student = 0
#     best_poz = -1
#     for i in range(len(students)):
#         if students[i].grade > best_student:
#             best_student = students[i].grade
#             best_poz = i
#     return students[best_poz]


if __name__ == '__main__':
    st = import_student('data/student.json')
    # print(st)
    print(find_best_student(st))

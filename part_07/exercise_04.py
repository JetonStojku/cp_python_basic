""" U 05 """
import json
from dataclasses import dataclass

"""
a) Ndertoni nje klas e cila do te ruaj elementet e json olymiad.json.
b) Ndertoni nje liste me objekte te importuara nga ky file.
c) Gjeni student me te mire.
d) Gjeni ekipin fitues. Ekipi (shteti) fitues perbehet nga 5 nxenesit me te mire te shtetit.
"""


@dataclass
class Student:
    point: int
    country: str
    last_name: str
    first_name: str


def convert_to_list_with_students(path: str) -> [Student]:
    with open(path) as f:
        students_dict_lst = json.load(f)
    return [Student(**student) for student in students_dict_lst]
    # return [Student(first_name=student['first_name'], last_name=student['last_name'], country=student['country'], point=student['point']) for student in students_dict_lst]


def create_countries(std: [Student]) -> {str: [int]}:
    countries = {}
    for student in std:
        if student.country in countries:
            countries[student.country].append(student.point)
        else:
            countries[student.country] = [student.point]
    return countries


def find_winner_country(countries):
    max_country = ('', 0)
    for country, students_point in countries.items():
        top_five_points = sum(sorted(students_point, reverse=True)[:5])
        if max_country[1] < top_five_points:
            max_country = (country, top_five_points)
    return max_country


students = convert_to_list_with_students('olympiad.json')

winner = max(students, key=lambda x: x.point)
print(winner)
countries = create_countries(students)
winner_country = find_winner_country(countries)
print(winner_country)

winner_country = max(countries.items(), key=lambda x: sum(sorted(x[1], reverse=True)[:5]))
print(winner_country)

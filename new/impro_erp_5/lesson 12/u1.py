""" u1 """
import json

"""
Në një json ruhen të dhënat e studentëve të një universiteti.
a) Ndërtoni një klasë e cila do të ruaj të dhënat e këtyre
    studentëve
b) Ndërtoni një klasë e cila do të ruaj emrin e shtetit dhe
    një listë me studentët e tij
c) Ndërtoni një funksion i cili kthen të dhënat e këtij json.
d) Ndërtoni një funksion i cili kthen një listë me
    studentë nga json i dhënë
e) Ndërtoni një metodë për studentët që kthen
    mesataren e tij
f) Gjeni studentin më të mirë
g) Gjeni kush prej gjinive ka mesatare më të lartë
h) Ndërtoni një metodë e cila kthen mesataren e shtetit
i) Ndërtoni një funksion i cili kthën një listë
    me shtete dhe studentët e secilit shtet
j) Ndërtoni një funksion i cili kthen shtetin
    me mesatare më të lartë
"""


class Student:
    def __init__(self, first_name, last_name, age, score, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.score = score
        self.gender = gender
        self.country = country

    def avg(self):
        return sum(self.score) / len(self.score)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}: {self.avg()}'


class Country:
    def __init__(self, name):
        self.name = name
        self.students = []

    def avg(self):
        count = 0
        s = 0
        for student in self.students:
            s += student.avg()
            count += 1
        return s / count

    def __repr__(self):
        return f"{self.name}: {self.avg()}"


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


def best_student(students: list[Student]) -> Student | None:
    if not students:
        return None
    best = students[0]
    for student in students:
        if student.avg() > best.avg():
            best = student

    return best


def is_female_greater(students: list[Student]) -> bool:
    sum_m = 0
    count_m = 0
    sum_f = 0
    count_f = 0
    for student in students:
        if student.gender == 'male':
            sum_m += student.avg()
            count_m += 1
        else:
            sum_f += student.avg()
            count_f += 1

    avg_male = sum_m / count_m if count_m != 0 else 0
    avg_female = sum_f / count_f if count_f != 0 else 0

    return avg_female > avg_male


def return_country_list(students: list[Student]) -> list[Country]:
    countries = []
    for student in students:
        not_find = True
        for country in countries:
            if student.country == country.name:
                country.students.append(student)
                not_find = False
                break
        if not_find:
            new_country = Country(student.country)
            new_country.students.append(student)
            countries.append(new_country)
    return countries


def return_country_list_2(students: list[Student]) -> list[Country]:
    countries: list[Country] = []
    countries_dict = {}
    for student in students:
        if student.country in countries_dict:
            countries[countries_dict[student.country]].students.append(student)
        else:
            new_country = Country(student.country)
            new_country.students.append(student)
            countries_dict[student.country] = len(countries)
            countries.append(new_country)
    return countries


def find_best_country(countries: list[Country]) -> Country:
    best = countries[0]
    for country in countries:
        if country.avg() > best.avg():
            best = country
    return best


student_json = import_json('student')
student_lst = create_students_list(student_json)
best_std = best_student(student_lst)
female = is_female_greater(student_lst)
print(student_json)
print(student_lst)
print(best_std)
print(female)
country_lst = return_country_list(student_lst)
print(country_lst)
country_lst_2 = return_country_list_2(student_lst)
print(country_lst)
best_country = find_best_country(country_lst_2)
print(best_country)

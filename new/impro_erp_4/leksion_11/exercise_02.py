""" u2 """
import json

"""
a) Ndërtoni një klasë që të ruaj objektet të tipit
    student që vijnë nga file olympiad.json
b) Ndërtoni një funksion i cili
    lexon dhe ruajini në një variabël të 
    dhënt që vijnë nga ky file
c) Ndërtoni një funksion i cili kthen një
    listë me objekte të tipit Student të
    importuara nga ky file.
d) Ndërtoni një funksion i cili kthen nxënësin
    më të mirë në olimpiad
e) 5 studentët më të mirë të çdo shteti përfaqsojnë
    shtetin me pikët e tyre. Ndërtoni një funksion
    i cili kthen shtetin fitues
    ku pikët e grumbulluara të çdo shteti janë
    shuma e pikëve të këtyre studentëve
"""


class Student:
    def __init__(self, first_name, last_name, country, point):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.point = point

    def __repr__(self):
        return f'/{self.first_name} {self.last_name} ({self.country}): {self.point}/'


def read_student(path):
    with open(f'data/{path}.json') as f:
        return json.load(f)


def return_student_list(lst_dict):
    lst = []
    for student_dict in lst_dict:
        student = Student(**student_dict)
        lst.append(student)
    return lst


def find_best_student(students: [Student]):
    best_student: Student = students[0]
    for student in students:
        if best_student.point < student.point:
            best_student = student
    return best_student


def group_by_country(students: [Student]):
    country_dictionary = {}
    for student in students:
        if student.country in country_dictionary:
            country_dictionary[student.country].append(student)
        else:
            country_dictionary[student.country] = [student]
    return country_dictionary


def find_country_points(students):
    for i in range(5):
        for j in range(i + 1, len(students)):
            if students[i].point < students[j].point:
                # temp = students[i]
                # students[i] = students[j]
                # students[j] = temp
                students[i], students[j] = students[j], students[i]
    s = 0
    for student in students[:5]:
        s += student.point
    return s


def find_best_country(students: [Student]):
    country_dict = group_by_country(students)
    best_country_point = -1
    best_country = ''
    for country, country_students in country_dict.items():
        if best_country_point < find_country_points(country_students):
            best_country_point = find_country_points(country_students)
            best_country = country
    return best_country, best_country_point


if __name__ == '__main__':
    std_dict_list = read_student('olympiad')
    print(len(std_dict_list))
    print('student number', '--' * 20)
    std_list = return_student_list(std_dict_list)
    print(std_list)
    print('list of students', '--' * 20)
    best_std = find_best_student(std_list)
    print(best_std)
    print('best student', '--' * 20)
    country_dict = group_by_country(std_list)
    print(country_dict)
    print('group by country', '--' * 20)
    best_country = find_best_country(std_list)
    print(best_country)
    print('best country', '--' * 20)

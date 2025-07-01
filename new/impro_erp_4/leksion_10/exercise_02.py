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


if __name__ == '__main__':
    std_dict_list = read_student('olympiad')
    print(len(std_dict_list))
    std_list = return_student_list(std_dict_list)
    print(std_list)

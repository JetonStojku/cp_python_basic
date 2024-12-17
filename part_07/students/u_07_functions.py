import json

from students.u_07_class import Student


def get_students_from_json(file_name: str) -> [dict]:
    with open(file_name, 'r') as file:
        students_dict = json.load(file)
    return students_dict


def convert_to_students_list(students_dict: [dict]) -> [Student]:
    # students = []
    # for student_dict in students_dict:
    #     student = Student(**student_dict)
    #     students.append(student)

    students = [Student(**student_dict) for student_dict in students_dict]

    return students


def get_female_percentage(students: [Student]) -> float:
    count_female = 0
    for student in students:
        if student.gender == 'female':
            count_female += 1
    return count_female / len(students)


def find_best_student(students: [Student]) -> float:
    best_student = students[0]
    for student in students:
        if student.avg() > best_student.avg():
            best_student = student
    return best_student


def group_student_by_country(students: [Student]) -> {str: [Student]}:
    countries = {}
    for student in students:
        if student.country not in countries:
            countries[student.country] = []
        countries[student.country].append(student)
    return countries

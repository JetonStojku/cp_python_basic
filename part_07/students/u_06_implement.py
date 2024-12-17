from u_06_functions import get_students_from_json, convert_to_students_list, get_female_percentage, find_best_student

students_dict = get_students_from_json(r'data/student.json')
students = convert_to_students_list(students_dict)
female_percentage = get_female_percentage(students)
print(f'Female percentage: {female_percentage: .2%}')

best_student = find_best_student(students)
print(best_student)

print('-' * 80)
nr_female = len(list(filter(lambda st: st.gender == 'female', students)))
female_percentage = nr_female / len(students)
print(f'Female percentage: {female_percentage: .2%}')

best_student = max(students, key=lambda st: st.grade)
print(best_student)

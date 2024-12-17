from u_07_functions import get_students_from_json, convert_to_students_list, get_female_percentage, find_best_student, \
    group_student_by_country

students_dict = get_students_from_json(r'data/student2.json')
students = convert_to_students_list(students_dict)
female_percentage = get_female_percentage(students)
print(f'Female percentage: {female_percentage: .2%}')

best_student = find_best_student(students)
print(best_student)

print('-' * 80)
nr_female = len(list(filter(lambda st: st.gender == 'female', students)))
female_percentage = nr_female / len(students)
print(f'Female percentage: {female_percentage: .2%}')

best_student = max(students, key=lambda st: st.avg())
print(best_student)

countries = group_student_by_country(students)

for country, st in countries.items():
    print(f'{country}: {len(st)}')

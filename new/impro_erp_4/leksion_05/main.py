class Person:
    def __init__(self, name, surname, age=18):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'{self.name} {self.surname}'


class Employee(Person):
    def __init__(self, name, surname, age, job, salary):
        super().__init__(name, surname, age)
        self.job = job
        self.salary = salary

    def raise_salary(self, x):
        self.salary *= (1 + x / 100)


p1 = Person('Test', 'Person', 30)
e1 = Employee('Test2', 'Employee', 28, 'programmer', 1500)
print(p1)
print(f'{e1} {e1.salary: .0f}')
e1.raise_salary(10)
print(f'{e1} {e1.salary: .0f}')

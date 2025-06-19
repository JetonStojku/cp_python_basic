""" u2 """
"""
Ndërtoni një klas të tipit Punonjës që ruan punonjësit
e një kompanie. Për çdo punonjës do ruhet:
emër, mbiemër, orë pune, paga orare.
metoda str duhet të ktheje emër mbiemër
ndërtoni një metodë e cila kthen sa lekë
ka për të marrë një punonjës.
"""


class Employee:
    def __init__(self, name, surname, work_hours, hourly_pay):
        self.name = name
        self.surname = surname
        self.work_hours = work_hours
        self.hourly_pay = hourly_pay

    def calc_salary(self):
        return self.work_hours * self.hourly_pay

    def __str__(self):
        return f"{self.name} {self.surname}"


e_1 = Employee("Bob", "Marley", 40, 10)
print(e_1, e_1.calc_salary())

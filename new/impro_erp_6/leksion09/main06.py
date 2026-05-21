from abc import ABC, abstractmethod


class Country(ABC):

    @abstractmethod
    def capital(self):
        pass

    @abstractmethod
    def language(self):
        pass

    @abstractmethod
    def type(self):
        pass


class India(Country):
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA(Country):
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
countries = (obj_ind, obj_usa)
for country in countries:
    country.capital()
    country.language()
    country.type()


# 2
def func(obj: Country):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

print('-' * 80)
for country in countries:
    func(country)

import json
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    citizenship: str
    worth: int


def import_persons(path: str) -> list[Person]:
    with open(path, 'r') as f:
        persons = json.load(f)

    # return [Person(person['name'], person['location']['citizenship'], person['wealth']['worth in billions']) for person in persons]

    lst = []
    for person in persons:
        name = person['name']
        citizenship = person['location']['citizenship']
        worth = person['wealth']['worth in billions']
        p = Person(name, citizenship, worth)
        lst.append(p)
    return lst


def top_wealthy_countries(persons: list[Person]) -> {str: int}:
    dict_countries = {}
    for person in persons:
        if person.citizenship in dict_countries:
            dict_countries[person.citizenship] += person.worth
        else:
            dict_countries[person.citizenship] = person.worth

    top_country = ''
    top_worth = 0
    for country, worth in dict_countries.items():
        if worth > top_worth:
            top_worth = worth
            top_country = country
    return (top_country, top_worth)


if __name__ == '__main__':
    persons = import_persons('billionaires.json')
    print(persons)
    print(top_wealthy_countries(persons))

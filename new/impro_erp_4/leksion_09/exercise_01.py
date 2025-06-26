""" Exercise 1"""
"""
a) Lexoni file cars.json dhe gjeni sa makina jane
b) Ndertoni një klase e cila do te ruaj në formë
    dictionary
    "Dimensions", "Engine Information",
    "Fuel Information", "Identification"
c) Ndërtoni një objekt makinë me të dhënat e
    makinës së parë nga file json
d) Ndërtoni një listë me objekte të tipit
    makinë ku të ruhen të gjitha makinat
    e ruajtura në file cars.json
e) Ndërtoni 4 klasa të tipit
    "Dimensions", "Engine Information",
    "Fuel Information", "Identification"
f) Ndërtoni një listë me objekte të tipit
    makinë ku të ruhen të gjitha makinat
    e ruajtura në file cars.json ku atributet
    janë objekte të tipve përkatëse
"""

import json


class Car:
    def __init__(self, dimensions, engine_information, fuel_information, identification):
        self.dimensions = dimensions
        self.engine_information = engine_information
        self.fuel_information = fuel_information
        self.identification = identification


with open('data/cars.json') as openfile:
    json_object = json.load(openfile)
print(len(json_object))
f1 = json_object[0]
print(f1['Dimensions'])
print('--' * 20)
print(f1['Engine Information'])
print('--' * 20)
print(f1['Fuel Information'])
print('--' * 20)
print(f1['Identification'])

audi = Car(f1['Dimensions'], f1['Engine Information'], f1['Fuel Information'], f1['Identification'])
print('==' * 20)
print(audi.dimensions)  # Dimension(height, length, width)
print('--' * 20)
print(audi.engine_information)
print('--' * 20)
print(audi.fuel_information)
print('--' * 20)
print(audi.identification)

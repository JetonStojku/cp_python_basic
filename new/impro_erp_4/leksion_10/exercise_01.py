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


class Dimensions:
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width


class EngineInformation:
    def __init__(self, driveline, engine_type, hybrid, number_of_forward_gears, transmission, engine_statistics):
        self.driveline = driveline
        self.engine_type = engine_type
        self.hybrid = hybrid
        self.number_of_forward_gears = number_of_forward_gears
        self.transmission = transmission
        self.engine_statistics = engine_statistics


class FuelInformation:
    def __init__(self, city_mpg, fuel_type, highway_mpg):
        self.city_mpg = city_mpg
        self.fuel_type = fuel_type
        self.highway_mpg = highway_mpg


class Identification:
    def __init__(self, classification, id, make, model_year, year):
        self.classification = classification
        self.id = id
        self.make = make
        self.model_year = model_year
        self.year = year


class Car:
    def __init__(self, dimensions: Dimensions, engine_information: EngineInformation, fuel_information: FuelInformation,
                 identification: Identification):
        self.dimensions = dimensions
        self.engine_information = engine_information
        self.fuel_information = fuel_information
        self.identification = identification

    def __repr__(self):
        return self.identification.model_year


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

# audi = Car(f1['Dimensions'], f1['Engine Information'], f1['Fuel Information'], f1['Identification'])
# print(audi)
# print('==' * 20)
# print(audi.dimensions)  # Dimension(height, length, width)
# print('--' * 20)
# print(audi.engine_information)
# print('--' * 20)
# print(audi.fuel_information)
# print('--' * 20)
# print(audi.identification)

# lst2 = []
# for el in json_object:
#     x = Car(el['Dimensions'], el['Engine Information'], el['Fuel Information'], el['Identification'])
#     lst2.append(x)


lst3 = []
for el in json_object:
    d_dict = el['Dimensions']
    e_dict = el['Engine Information']
    f_dict = el['Fuel Information']
    i_dict = el['Identification']
    dimensions = Dimensions(d_dict['Height'], d_dict['Length'], d_dict['Width'])
    engine_information = EngineInformation(e_dict['Driveline'], e_dict['Engine Type'], e_dict['Hybrid'],
                                           e_dict['Number of Forward Gears'], e_dict['Transmission'],
                                           e_dict['Engine Statistics'])
    fuel_information = FuelInformation(f_dict['City mpg'], f_dict['Fuel Type'], f_dict['Highway mpg'])
    identification = Identification(i_dict['Classification'], i_dict['ID'], i_dict['Make'], i_dict['Model Year'],
                                    i_dict['Year'])
    x = Car(dimensions, engine_information, fuel_information, identification)
    lst3.append(x)

print(lst3)

import json
from dataclasses import dataclass

POINTS = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1)


@dataclass
class GrandPrix:
    fastest_time: list[float]
    laps_time: list[float]


class Pilot:
    def __init__(self, name: str, location: str, id: int, grand_prix: list[{str: list[float]}]):
        self.name = name
        self.location = location
        self.id = id
        self.gps = [GrandPrix(**gp) for gp in grand_prix]
        self.points = []

    def get_fastest_time(self, gp_index: int):
        return min(self.gps[gp_index].fastest_time)

    def get_laps_time(self, gp_index: int):
        return sum(self.gps[gp_index].laps_time)

    def get_points(self):
        return sum(self.points)

    def __repr__(self):
        return f"|{self.name}: {self.get_points()}|"


def get_pole_position(pilots: [Pilot], gp_index: int):
    return min(pilots, key=lambda pilot: pilot.get_fastest_time(gp_index))


def get_grand_prix_winner(pilots: [Pilot], gp_index: int):
    return min(pilots, key=lambda pilot: pilot.get_laps_time(gp_index))


def set_points(pilots: [Pilot], gp_index: int):
    sorted_pilots_grand_prix = sorted(pilots, key=lambda pilot: pilot.get_laps_time(gp_index))
    pole_position_pilot = get_pole_position(pilots, gp_index)
    for i, pilot in enumerate(sorted_pilots_grand_prix[:10]):
        pilot.points.append(POINTS[i] + (pole_position_pilot.id == pilot.id))
    for i, pilot in enumerate(sorted_pilots_grand_prix[10:]):
        pilot.points.append(0)


def return_final_classification(pilots: [Pilot]):
    return sorted(pilots, key=lambda pilot: pilot.get_points(), reverse=True)


with open('datas/formula_one_pilots.json', 'r') as f:
    data = json.load(f)

all_pilots = [Pilot(**pilot) for pilot in data]
first_place = get_grand_prix_winner(all_pilots, 0)

total_grand_prix = len(all_pilots[0].gps)

for index in range(total_grand_prix):
    set_points(all_pilots, index)

final_classification = return_final_classification(all_pilots)
first_grand_prix_sorted = sorted(all_pilots, key=lambda pilot: pilot.get_laps_time(0))
for i in range(len(first_grand_prix_sorted)):
    print(f"{i + 1}. {first_grand_prix_sorted[i].name}: {first_grand_prix_sorted[i].get_laps_time(0): .2f}")

print(first_place)
print(all_pilots)
print(final_classification)

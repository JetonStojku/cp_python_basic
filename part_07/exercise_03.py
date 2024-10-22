import json


def get_max_delayed(airlines):
    max_airline = airlines[0]
    for airline in airlines:
        max_val = max_airline['Statistics']['Minutes Delayed']['Total']
        airline_val = airline['Statistics']['Minutes Delayed']['Total']
        if max_val < airline_val:
            max_airline = airline
    return max_airline


with open('airlines.json', 'r') as f:
    airlines = json.load(f)

print(get_max_delayed(airlines))

max_airline = max(airlines, key=lambda x: x['Statistics']['Minutes Delayed']['Total'])
print(max_airline)

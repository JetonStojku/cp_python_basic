import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500",
    "test": [1, 2, 3],
    "true": True,
    "false": False,
    "none": None,
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
with open("data/sample.json", "w") as outfile:
    outfile.write(json_object)

with open("data/sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

with open('sample.json') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

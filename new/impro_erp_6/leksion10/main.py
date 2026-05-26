import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500",
    "True": True,
    "None": None,
}

json_object = json.dumps(dictionary, indent=4)

with open("data/sample.json", "w") as outfile:
    outfile.write(json_object)

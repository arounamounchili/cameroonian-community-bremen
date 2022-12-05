"""
JSON
"""

import  json

# Parse JSON String
person1 = '{"firstname": "Inteligencia", "lastname": "Mounchili", "age": 24}'
parser_person1 = json.loads(person1)
print(parser_person1["firstname"])

# Convert object to JSON String
person2 = {
    "firstname": "Inteligencia",
    "lastname": "Mounchili",
    "age": 24
}

# convert into JSON
convert_to_json = json.dumps(person2)
print(convert_to_json)
print()

# Convert Python objects into JSON Strings
print(json.dumps({"firstname": "Inteligencia", "lastname": "Mounchili"}))
print(json.dumps(["firstname", "Inteligencia", "lastname"]))
print(json.dumps(("firstname", "Inteligencia")))
print(json.dumps("Inteligencia"))
print(json.dumps(444))
print(json.dumps(2344.5))
print(json.dumps(True))
print(json.dumps(None))
print()

# Format the result
print(json.dumps({"firstname": "Inteligencia", "lastname": "Mounchili"}, indent=2))

# json - dane typu klucz - wartość
# używamy w komunikacji pomiędzy sytemai w internecie
# odpowiednikiem json ajest słownik
# {
#   "menu": {
#     "id": "file",
#     "value": "File",
#     "popup": {
#       "menuitem": [
#         {"value": "New", "onclick": "CreateNewDoc()"},
#         {"value": "Open", "onclick": "OpenDoc()"},
#         {"value": "Close", "onclick": "CloseDoc()"}
#       ]
#     }
#   }
# }

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortowanie po kluczach
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', "r") as f:
    data = json.load(f)

print(data)
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>

print(data['name'])  # Radek

# słownik - para klucz - wartosc
# {"user": "Radek", "wiek": 35}
# klucze nie mogą sie powtarzać
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 45
print(dictionary)  # {'imie': 'Radek', 'wiek': 45}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 45])
# dict_items([('imie', 'Radek'), ('wiek', 45)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 45}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'

print(dictionary.get("imie"))  # Tomek
print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default, dostaliśmy domyślną wartość

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower())  # False
""" Return a version of the string suitable for caseless comparisons. """
print(name1.casefold() == name2.casefold())  # True

dictionary.update({"date": "12-12-2050"})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 45, 'date': '12-12-2050'}

dict_small = {'x': 2}
dict_small.update([("y", 3), ("z", 8)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 8}

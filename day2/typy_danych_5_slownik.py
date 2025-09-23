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

# # input() - pozwala wprowadzac dane np.: z kalwiatury
# tekst = input("Podaj imię:")
# print(tekst)
# # Podaj imię:Radek
# # Radek

# # napisać aplikację kalkulator
# a = int(input("Podaj pierwszą liczbę:"))
# b = float(input("Podaj drugą liczbę:"))
# print(a + b)
# print(int(a) + float(b))
# # Podaj pierwszą liczbę:56
# Podaj drugą liczbę:212
# 268.0
# 268.0

# napisać aplikację słownik pol-ang
# zestawnych danych -> słownik
# wyswietlic klucze
# przyjąc słowko od użytkownika - input()
# wyświetlić tłumaczenie
pol_ang = {'pies': 'dog', "kot": "cat", "dach": "roof"}
print("Znam takie słówka:", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia:")
# print(pol_ang[odp])
# print(pol_ang.get(odp.strip().casefold(), "Nie ma w słowniku"))
print(f"Prawidłowa odpowiedz dla: {odp} to: {pol_ang.get(odp.strip().casefold(), "Nie ma w słowniku")}")
# Znam takie słówka: dict_keys(['pies', 'kot', 'dach'])
# Podaj słówko do przetłumaczenia:kot
# Prawidłowa odpowiedz dla: kot to: cat

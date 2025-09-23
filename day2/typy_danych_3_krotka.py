# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzać pamiecią
# krotka jedoelementowa - stała, szczególny przykłąd zmiennej

tupla_imiona = "Zenek", 'Marek', "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))
print(tupla_liczby)
# <class 'tuple'>
# (43, 55, 22.34, 11, 200)

tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))
print(tupla_liczby)
# <class 'tuple'>
# (43, 55, 22.34, 11, 200)

# tupla jedoelementowa
tupla_jeden = 45,
print(tupla_jeden)
print(type(tupla_jeden))
# (45,)
# <class 'tuple'>

# PEP8 zalecaa by tuple jedoelementową tworzyć z nawiasem
tupla_jeden = (45,)
print(type(tupla_jeden))
print(tupla_jeden)
# <class 'tuple'>
# (45,)

# tupla jest niemutowalna
# TypeError: 'tuple' object does not support item assignment
# tupla_jeden[0] = 123

# usunięcie całej tupli
del tupla_jeden

# po usunięciu tupli, nie istnieje
# print(tupla_jeden) # NameError: name 'tupla_jeden' is not defined

print(tupla_imiona.index("Radek"))  # index numer 2
print(tupla_imiona.count("Radek"))  # występuje 1 raz

print(len(tupla_imiona))  # długość 4

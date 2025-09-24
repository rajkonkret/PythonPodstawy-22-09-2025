dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisanie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisze pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.

for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
for k, v in dictionary.items():
    print(k, v, sep="=>", end="<===>")
    # imie=>Radek<===>nazwisko=>Kowalski<===>
print("Radek")  # imie=>Radek<===>nazwisko=>Kowalski<===>Radek
print("tomek")
# imie=>Radek<===>nazwisko=>Kowalski<===>Radek
# tomek

pol_ang = {'pies': 'dog', "kot": "cat", "dach": "roof"}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k  # wartość staje się kluczem a klucz staje się wartością
print(ang_pol)  # {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

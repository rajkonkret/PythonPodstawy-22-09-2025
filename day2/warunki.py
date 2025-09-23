# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# warunek musi zwracać typ bool (prawda, fałsz) True, False

odp = True
print(bool(True))  # True
odp = False
# debugger, pułąpka
if odp:
    # blok programu wykonywany gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print('Dalsza częśc programu niezależna od warunku')
# True
# Dalsza częśc programu niezależna od warunku

odp = "Radek"
print(bool(odp))  # True

if odp:
    print('Dane zostały wczytane')
    # Dane zostały wczytane

if odp == "Radek":  # porównanie
    print("Jesteś Radek")
# Jesteś Radek

odp = 0
if odp:
    print("Działa")
else:  # w przeciwnym wypadku
    print("Zero -> False")
# Zero -> False

a = "Radek"
if len(a) > 3:
    print(f"Długość wynosi {len(a)}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
# Długość wynosi 5, więcej niż 3

# podatek = 0
# zarobki = int(input("Podaj zarobki:"))
#
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 50_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else: # pozostałę
#     podatek = 0.9
#
# print(f'Podatek wynosi {zarobki * podatek} pln.')
# # podatek 0.2 dla przedziału 10_000 do 49_999
# ctrl / - komentarz

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0
print(f'Rabat wynosi {rabat}')  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print(f'Rabat wynosi {rabat}')  # Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienna przchowująca typ systemu
# console, email, inny

# console: "Stało się coś strasznego"
# email: "System email"
# dla systemu email do listy błędów wpisać opis błedu
alert_system = "email"  # console, email, inny
lista_b = []
error = "error"  # error, medium, inny
if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Inny system")

print("Lista błędów:", lista_b)
# Stało się coś strasznego
# Lista błędów: []
# System email
# Lista błędów: ['Krytyczny']

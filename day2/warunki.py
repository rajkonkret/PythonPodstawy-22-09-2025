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

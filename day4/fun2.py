# funkcje zwracające wynik
# kończy się za pomocą return

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(6, 8))  # 14
wynik = dodaj(6, 90)
print("Wynik:", wynik)  # Wynik: 96
#
print(odejmij())  # 0
print(odejmij(a=7, b=9, c=0))  # -2
print(odejmij(1, 2, 3))  # -4
print(odejmij(1, 2))  # -1
print(odejmij(1, b=9, c=90))  # -98


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))
print(oblicz_vat(vat=9, kwota=3500))
# 1230.0
# 1150.0
# 3815.0

zm = oblicz_vat(1000)  # 1230.0
if zm == 1230:
    print("Ok")  # Ok

print(dodaj(5, 7) + odejmij(5, 6))  # 11

# funkcja lambda
# skrócony zapis funkcji
# domyślnie lambda zwraca wynik (return)
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b  # domyślnie posiada return
print(odejmij2(10, 8))  # 2

# przerobić na lmbdę oblicz_vat
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100
oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
# 1230.0
# 1080.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

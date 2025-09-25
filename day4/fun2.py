# funkcje zwracające wynik
# kończy się za pomocą return

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(6, 8))  # 14
wynik = dodaj(6, 90)
print("Wynik:", wynik)  # Wynik: 96

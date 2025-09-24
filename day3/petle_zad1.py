# pętla - pozwala wielokrotnie wykonać fragment kodu
# for - pętla iteracyjna
import random

from day3.random_zad1 import lista

for i in range(5):  # od 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    print(_)

for i in range(5):
    print(i + 2)
    print(i * 2)

#  przerobić na pętle lotto
lista_kula = list(range(1, 50))
lista_wyn = []
for _ in range(6):  # sześć razy
    wyn = random.choice(lista_kula)
    lista_kula.remove(wyn)
    print(wyn)  # 39
    lista_wyn.append(wyn)

print(lista_wyn)  # [49, 46, 11, 44, 43, 36]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzyste")
# 0 parzyste
# 2 parzyste
# 4 parzyste
# 6 parzyste
# 8 parzyste

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]

for c in lista3:  # wyciągnie wszystkie elementy z listy, pod c podstawia eleemnt
    print(c)

lista_nazwy = ["Ala", 'Tomek', 'Zenek']
for o in lista_nazwy:
    print(o)
# Ala
# Tomek
# Zenek

for c in lista3:  # wyciągnie wszystkie elementy z listy, pod c podstawia eleemnt
    if c > 4:
        print(c, "Wieksze od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "Mniejsze od 4")
    print(c)
# 0 Mniejsze od 4
# 0
# 2 Mniejsze od 4
# 2
# 4 Równe 4
# 4
# 6 Wieksze od 4
# 6
# 8 Wieksze od 4
# 8

for i in range(0, 10, 2):  # (start,stop,krok)
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # ujemny krok, odliczanie w dół
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)  # dla c==2
    print("Wykona dla każdego przejscia pętli")
print("Po zakończeniu pętli")
# Wykona dla każdego przejscia pętli
# 3
# Wykona dla każdego przejscia pętli
# Wykona dla każdego przejscia pętli
# Wykona dla każdego przejscia pętli
# Wykona dla każdego przejscia pętli
# Po zakończeniu pętli

imiona = ["Radek", "Tomek", "Agata", "Marek"]
print(imiona)  # ['Radek', 'Tomek', 'Agata', 'Marek']
print(type(imiona))  # <class 'list'>

# wypisac jedno pod drugim elementy z listy
for p in imiona:
    print(p)
# Radek
# Tomek
# Agata
# Marek

# 0 Radek
for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

# enumerate() - numeruje i zwraca numer i element kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Agata')
# (3, 'Marek')

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Agata
# 4 Marek

# imiona = ["Radek", "Tomek", "Agata", "Marek"]
imiona = ["Radek", "Tomek", "Agata", "Marek", "Anna"]
wiek = [44, 56, 23, 34]

# # Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
#     # IndexError: list index out of range dla różnych długości list
# # Radek 44
# # Tomek 56
# # Agata 23
# # Marek 34

# zip() - łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 34)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 56
# Agata 23
# Marek 34

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 56))
# (2, ('Agata', 23))
# (3, ('Marek', 34))
# (0, ('Radek', 44))

a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)
a, (b, d) = (0, ('Radek', 44))
for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 56
# 2 Agata 23
# 3 Marek 34

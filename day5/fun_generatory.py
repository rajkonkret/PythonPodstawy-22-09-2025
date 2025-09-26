# generatory - funkcje, które zwracają kolejne wynik
# nie przechowuje kolejnych wyników
# podstawia w kolejności (dostęp sekwencyjny)
#  efektywnie zarzadza pamięcią
# leniwe - generowanie - dane dostarczane są tylko wtedy kiedy są potrzebne

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# 0
# 1
# 4
# 9
# 16

# generator
def kwadrat2(n):
    for x in range(n):
        # zwraca wynik, zatrzymuje się,
        # pamięta gdzie zatrzymał,
        # nastepne wywołanie podaje koleny wynik
        yield x ** 2


kwa = kwadrat2(5)
print(type(kwa))  # <class 'generator'>

# wyświetla kolejny wynik z generatora
print(next(kwa))
print(next(kwa))
print(next(kwa))
# 0
# 1
# 4
print("Zrób cokolwiek")
lista = []
lista.append("Radek")
print(lista)
# generator kontunuuje od miejsca zatrzymania
print(next(kwa))
print(next(kwa))
# 9
# 16
# generator kończy działąnie rzucając wyjąte: StopIteration
# print(next(kwa))
try:
    print(next(kwa))
except StopIteration:
    print("Koniec generatora")


# Koniec generatora

# generator bez końća
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


def count_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


c2 = count_down(10)
print(next(c2))
print(next(c2))
print(next(c2))
print(next(c2))

# wyciąga wszystkie dane z generatora, nie rzuci StopIteration
for i in count_down(10):
    print(i)


def counter2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == "q":
            break
        n += 1


c3 = counter2(10)
print(next(c3))
print(next(c3))
print(next(c3))
print(next(c3))

c3.send('Ok')
print(next(c3))  # Ok

try:
    c3.send("q")  # StopIteration
except StopIteration as e:
    print("Koniec dnaych:", e)
# q
# Koniec dnaych:

# funkcja - wydzielony fragment programu, można użyc w dowolnym momencie
# funkcja musi być najpierw zadeklarowana
# żeby użyć funkcji trzeba ją wywołać

a = 8
b = 6


# funkcje niezwracające wyniku
# deklaracja funkcji
# PEP8 prosi by deklaracja funkcji była oddzielona dwoma pustymi liniami
def dodaj():
    print(a + b)  # przyjęła waartości globalnych zmiennych o tej nazwie


def dodaj2(a, b):  # dwa argumenty, obowiązkowo do przekazania przy wywołaniu
    print(a + b)


# pozwala zasymulować przeciążenie funkcji liczbą argumentówg
def odejmij(a, b, c=0):  # c=0 a rgument o wartości domyslnej
    print(a - b - c)


# przekazanie argumentów po pozycji
# użycie funkcji (wywołanie)
dodaj()  # 14

# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(45, 78)  # 123

odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4, c=3

# przekazywanie po nazwie (keywords)
odejmij(b=8, a=0, c=10)  # -18
dodaj2(b=9, a=8)  # 17

# mieszane
odejmij(1, 2, c=78)  # -79
dodaj2(1, b=9)  # 10

# pozycyjne muszą byc przed nazwanymi
# odejmij(a=0, 1, 2) # SyntaxError: positional argument follows keyword argument

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# funkcja nie zwraca wyniku, zwraca None
# print(dodaj() + dodaj2(5, 9))

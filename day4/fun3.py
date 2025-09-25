a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne, nie wpłyną na zmienne globalne o tej samej nazwie
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # użyje globalnych


def dodaj3():
    global a  # użyj globalnej zmiennej a
    a = 9
    b = 90  # zmienna lokalna
    print(a + b)


print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj()  # 15, na lokalnych wartościach
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj2()  # 20, na globalnych wartościach
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 10 (globalna)
dodaj3()  # 99, wykonane na wartościach z funkcji ale zmieniło wartość globalną a
print(f"Wartość a z góry: {a} (globalna)")  # Wartość a z góry: 9 (globalna)
# a=9, b=10
dodaj2()  # 19

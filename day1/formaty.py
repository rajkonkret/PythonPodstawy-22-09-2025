user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001
print(type(wersja))  # <class 'float'>, zmiennoprzecinkowe

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# %s - łańcuch znaków (string)
# %d: formatowanie liczb całkowitych
# %f: formatowanie liczb zmiennoprzecinkowych
# %i - liczba całkowita (integer)
# TypeError: %d format: a real number is required, not str
# python sprawdza typy
# print("Witaj %d, masz teraz %s lat." % (user, wiek))

print("Witaj %(user)s, jesteś %(user)s" % {"user": user})
# Witaj Tomek, jesteś Tomek
print("Witaj %(user)a, jesteś %(user)a" % {"user": user})
# Witaj 'Tomek', jesteś 'Tomek'

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.

print('Używamy wersji pythona %i' % 3)  # Używamy wersji pythona 3
print('Używamy wersji pythona %f' % 3)  # Używamy wersji pythona 3.000000
print('Używamy wersji pythona %.2f' % 3)  # Używamy wersji pythona 3.00
print('Używamy wersji pythona %.1f' % 3.9)  # Używamy wersji pythona 3.9
print('Używamy wersji pythona %.0f' % 3.9)  # Używamy wersji pythona 4 - zaokrągli
print('Używamy wersji pythona %.f' % 3.9)  # Używamy wersji pythona 4 - zaokrągli
# zaokrągla do wyświetlania

x = 3.8769
print(x)
print(f"{x:.2f}")  # 3.88 str
print(x)  # 3.8769 - liczba się nie zmieni
y = round(x)
print(y)  # 4 int, <class 'float'>
z = round(x, 2)
print(f"{z=}")  # z=3.88, z pozostaje <class 'float'>
print(type(z))  # <class 'float'>
# ctrl alt l - formatowanie wg PEP8

print(f'Używamy wersji pythona {wersja}')  # Używamy wersji pythona 3.900001
print(f'Używamy wersji pythona {wersja:.2f}')  # Używamy wersji pythona 3.90
print(f'Używamy wersji pythona {wersja:.1f}')  # Używamy wersji pythona 3.9
print(f'Używamy wersji pythona {wersja:.0f}')  # Używamy wersji pythona 4

print(f'{user:<10}')  # "Tomek     "
print(f"{user:>15}")  # "          Tomek"
print(f'{user:^20}')  # "       Tomek        "

liczba = 678654345321
print(liczba)  # 678654345321
print(f'Nasza duża liczba: {liczba:,}')  # Nasza duża liczba: 678,654,345,321
print(f'Nasza duża liczba: {liczba:_}')  # Nasza duża liczba: 678_654_345_321
print(f'Nasza duża liczba: {liczba:_}'.replace("_", " "))  # Nasza duża liczba: 678 654 345 321
print(f'Nasza duża liczba: {liczba:_}'.replace("_", "."))  # Nasza duża liczba: 678.654.345.321

liczba = 150_000_000
print(liczba)  # 150000000
print(type(liczba))  # <class 'int'>

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

print('')

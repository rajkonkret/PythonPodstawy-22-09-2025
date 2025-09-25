# klasa - element programowania obiektowego
# klasa - przepis, szablon
# cechy (zmienne)
# metody - funkcje w klasie
# obiekt - instancja klasy
# kalsa musi zostać zadeklarowana przed użyciem
# tworzenie oboektu klasy uruchamia funkcję inicjalizującą (konstruktor) __init__
# paradygmaty -> hermetyzacja, dziedziczenie,  polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f'Nazywam się: {self.imie}')
        # print(f'Nazywam się: {cz1.imie}')


print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
# Prints the values to a stream, or to sys.stdout by default.
#
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.

#  cd .. - wyjscie z katalogu
#  cd day4 - wejście do katalogu day4
#  pydoc -b - serwer dokumentacji
#  pydoc -w kl1 - generuje plik kl1.html z dokumentacja

# tworzenie obiektu klasy Human
cz1 = Human()
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k
cz1.wiek = 50
cz1.imie = "Anna"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 50
# k

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 56
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Radek
# 56
# m
cz1.powitanie()
cz2.powitanie()
# Nazywam się: Anna
# Nazywam się: Radek

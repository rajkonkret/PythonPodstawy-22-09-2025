from abc import ABC, abstractmethod


# klasa abstrakcyjna - klasa z której nie można stworzyć obiektu
# klasa jest abstrakcyjna gdy posiada metode abstrakcyjną
class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc)

    @abstractmethod  # dekorator, oznacza klasę abstrakcyjną
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura, dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        # gdy zmieniamy konstruktor w klasie dziedziczącej
        # obowiązowo musimy uzyć konstruktora z klasy nadrzędnej
        # jest to słówko super()
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("ko ko ko ko")


class Orzel(Ptak):
    """
    Dziedziczy po Ptak
    """

    def wydaj_odglos(self):
        print("Kir kier kir kir")


class Wrona(Ptak):
    """
    Klasa Wrona, dziedziczy po Ptak
    Nie zadziała
    Brak metody wydaj_odglos()
    """


# niemożna tworzyć obiektów klasy abstrakcyjnej!!!
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# orzel = Ptak("Orzel", 45)
# orzel.latam()  # Tu Orzel Lecę z szybkością: 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością: 0
# print("Odgłos kura 1:", kur1.wydaj_odglos())

kur2 = Kura("Kura Zielononóżka")
kur2.latam()  # Tu Kura Zielononóżka Ja nie latam.

or2 = Orzel("Orzel Bielik", 55)
or2.latam()  # Tu Orzel Bielik Lecę z szybkością: 55
print("Odgłos kura 2:", kur2.wydaj_odglos())
print("Odgłos orzel 2:", or2.wydaj_odglos())
# Tu Orzel Lecę z szybkością: 45
# Tu Kura Lecę z szybkością: 0
# Odgłos kura 1: None
# Tu Kura Zielononóżka Ja nie latam.
# Tu Orzel Bielik Lecę z szybkością: 55
# ko ko ko ko
# Odgłos kura 2: None
# Kir kier kir kir
# Odgłos orzel 2: None

# TypeError: Can't instantiate abstract class Wrona without an implementation for abstract method 'wydaj_odglos'
# wrona1 = Wrona("Wrona", 24)

# polimorfizm - obiektu róznych kals, dzieki wspolnej klasie abstrakcyjnej mają wspolne elementy
# mogą być traktowane w penym zakresie jako obiekty wspołnej klasy Ptak.
lista = [or2, kur2]  # to są obiekty dwóch różnych klas
for i in lista:
    i.wydaj_odglos()
# Kir kier kir kir
# ko ko ko ko

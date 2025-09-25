class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor - metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # hermetyzacja
        # pole prywatne
        self.__predkosc = 0

    # zabezpieczenie pól i wystawienie metod do odczytu i zapisu - enkapsulacja
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h.")

    def hamulec(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Golf", 2025)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# print(car.__predkosc)  # 50
car.licznik()  # Prędkość wynosi: 50 km/h.
car.__predkosc = 0
car.licznik()  # Prędkość wynosi: 50 km/h.
car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.licznik()  # Prędkość wynosi: 0 km/h.
# AttributeError: 'Car' object has no attribute '__zmien_bieg'. Did you mean: '_Car__zmien_bieg'?
# car.__zmien_bieg()
# Prędkość wynosi: 50 km/h.
# Prędkość wynosi: 50 km/h.
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi: 0 km/h.

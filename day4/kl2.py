class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f'Nazywam się: {self.imie}')
        # print(f'Nazywam się: {cz1.imie}')

    # wypisz_wiek(), wypisz_wzrost()
    def wypisz_wzrost(self):
        print(f'Mam {self.wzrost} cm wzrostu.')

    def wypisz_wiek(self):
        print(f'Mam {self.wiek} lat.')

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
# cz1 = Human()

cz1 = Human("Anna", 45, 167)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Anna
# 45
# 167
# k

cz2 = Human("Radek", 45, 190, "m")
print(cz2.imie)
print(cz2.wiek)
print(cz2.wzrost)
print(cz2.plec)
# Radek
# 45
# 190
# m

cz1.powitanie()
cz2.powitanie()
# Nazywam się: Anna
# Nazywam się: Radek
cz1.wypisz_wzrost()
cz2.wypisz_wzrost()

cz1.wypisz_wiek()
cz2.wypisz_wiek()
# Mam 167 cm wzrostu.
# Mam 190 cm wzrostu.
# Mam 45 lat.
# Mam 45 lat.

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę

# stworzyć funkcję kantor
# ma mieć dwie wewnętrzne funkcje: usd, eur
# w zależności od parametru ma zwrócić jedną lub drugą funkcję
# przekazenie kwoty do funkcji wew

def kantor(waluta):
    def usd(kwota=0):
        print(f"Zamiana {kwota} usd na {kwota * 3.63} pln.")

    def eur(kwota=0):
        print(f"Zamiana {kwota} eur na {kwota * 4.26} pln.")

    if waluta == "eur":
        return eur  # zwracam adres funkcji
    else:
        return usd


kantor_usd = kantor("usd")
kantor_usd(10000)  # Zamiana 10000 usd na 36300.0 pln.

kantor_eur = kantor("eur")
kantor_eur(2500)  # Zamiana 2500 eur na 10650.0 pln.

kantor_usd(500)
kantor_eur(500)
# Zamiana 500 usd na 1815.0 pln.
# Zamiana 500 eur na 2130.0 pln.

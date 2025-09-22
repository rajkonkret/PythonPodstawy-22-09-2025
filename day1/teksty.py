tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())
zm = tekst.upper()  # WITAJ ŚWIECIE
print(zm)
# WITAJ ŚWIECIE
# WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie - pierwsza litera w zdaniu dużymi
print(tekst)  # Witaj Świecie

# Witaj Świecie
# 0123456789....... indeksy numerowane od 0
print(tekst[2])  # t

print(tekst.index("Ś"))  # 6

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j",0,4))# 0, z prawej zbiór otwarty, indeksy 0123

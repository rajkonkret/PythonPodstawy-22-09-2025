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
print(tekst.count("j", 0, 4))  # 0, z prawej zbiór otwarty, indeksy 0123

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków, spacji, na początku i końcu tekstu
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie' dane typu bajtowego
# \xc5\x9a zapis w sytemie szesnastkowym literki "Ś"
print(type(encode_s))  # <class 'bytes'>
print(encode_s.decode("utf-8"))  # Witaj Świecie

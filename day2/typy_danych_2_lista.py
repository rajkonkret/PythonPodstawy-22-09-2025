# kolekcje

# lista - przechowuje dowolną ilośc danych, różnego typu na raz
# zachowuje kolejność przy dodawaniu elementów

# pusat lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(lista)  # []
print(type(lista))  # <class 'list'>

# append() - dodawanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Kamil")
lista.append("Adam")
lista.append("Anita")
lista.append("Agata")

print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Kamil', 'Adam', 'Anita', 'Agata']
#     0        1        2        3        4       5        6

print(len(lista))  # mamy 7 elementów

print(lista[2])  # Zenek, trzeci element
print(lista[4])  # Adam

# print(lista[10])  # IndexError: list index out of range
# # ['Radek', 'Tomek', 'Zenek', 'Kamil', 'Adam', 'Anita', 'Agata']
# #     0        1        2        3        4       5        6
# #     -7       -6       -5       -4       -3      -2       -1
print(lista[6])  # Agata
print(lista[len(lista) - 1])  # Agata
print(lista[-1])  # Agata, ostatni element z listy
print(lista[-3])  # Adam

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']

print(lista[2:])  # ['Zenek', 'Kamil', 'Adam', 'Anita', 'Agata'], z ostanim włącznie
print(lista[2:6])  # ['Zenek', 'Kamil', 'Adam', 'Anita'], bez ostatniego

print(lista[2:20])  # ['Zenek', 'Kamil', 'Adam', 'Anita', 'Agata'] wyświetli dostępne
print(lista[12:45])  # []

print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Kamil', 'Adam', 'Anita', 'Agata']

# # ['Radek', 'Tomek', 'Zenek', 'Kamil', 'Adam', 'Anita', 'Agata']
# #     0        1        2        3        4       5        6
# #     -7       -6       -5       -4       -3      -2       -1
print(lista[-2:0])  # [], [5:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Kamil', 'Adam'], [0:5]

# range() - generuje liczby z zakresu
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[0:15:2])  # [0, 2, 4, 6, 8, 10, 12, 14] [start:stop:krok]

print(lista[::2])  # ['Radek', 'Zenek', 'Adam', 'Agata']
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14], generowany co drugi

# wyświetli listę w odwrotnej kolejności - idzie od końca
print(lista[::-1])  # ['Agata', 'Anita', 'Adam', 'Kamil', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elementu w liście na wskazanym indeksie
# zmiana w oryginalnej liście
lista[3] = "Asia"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Asia', 'Adam', 'Anita', 'Agata']

# wstawienie elementu na wskazanym indeksie
lista.insert(1, "Ola")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Zenek', 'Asia', 'Adam', 'Anita', 'Agata']

# usunięcie elemntu z listy, po elemencie, pierwszy napotkany
lista.remove("Tomek")
print(lista)  # ['Radek', 'Ola', 'Zenek', 'Asia', 'Adam', 'Anita', 'Agata']
lista.append("Zenek")
print(lista)
lista.remove("Zenek")
print(lista)  # ['Radek', 'Ola', 'Asia', 'Adam', 'Anita', 'Agata', 'Zenek']

# usunięcie po indeksie
# pop() - zwraca usunięty element
print(lista.pop(2))  # Asia, wypisze usunięty element
zmienna = lista.pop(-1)
print("Zmienna:", zmienna)  # Zmienna: Zenek
print(lista)  # ['Radek', 'Ola', 'Adam', 'Anita', 'Agata']
print(lista.pop())  # Agata, usunie ostatni element

# sprawdzenie indexu dla danego elementu
print(lista.index("Anita"))  # indeks 3, pierwszy napotkany

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista_2 = lista  # kopia adresu listy, kopia referencji
print(lista)  # ['Radek', 'Ola', 'Adam', 'Anita']
print(lista_2)  # ['Radek', 'Ola', 'Adam', 'Anita']

lista_copy = lista.copy()  # kopia elementow listy
lista.clear()  # czyszczenie elementów listy
print(lista)  # []
print(lista_2)  # []
print(lista_copy)  # ['Radek', 'Ola', 'Adam', 'Anita']
# id() - pokazuje miejsce w pamięci
print(id(lista))  # 2481663485056
print(id(lista_2))  # 2481663485056
print(id(lista_copy))  # 2481697537792

liczby = [54, 999, 34, 12.34, 567, 999]
print(liczby)  # [54, 999, 34, 12.34, 567, 999]
print(type(liczby))  # <class 'list'>

liczby.sort()  # posortował oryginalną listę
print(liczby)  # [12.34, 34, 54, 567, 999, 999]

liczby = [54, 999, 34, 12.34, 567, 999, "A"]
print(liczby)  # [54, 999, 34, 12.34, 567, 999, 'A']
print(type(liczby))  # <class 'list'>

# liczby.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)  # ['Radek', 'Ola', 'Adam', 'Anita']
lista_copy.sort()
print(lista_copy)  # ['Adam', 'Anita', 'Ola', 'Radek'] # alfabetycznie

lista_copy.sort(reverse=True)  # sortuje i odwraca
print(lista_copy)  # ['Radek', 'Ola', 'Anita', 'Adam']

lista_copy.reverse()  # odwraca bez sortowania
print(lista_copy)  # ['Adam', 'Anita', 'Ola', 'Radek']

liczby[3] = 666
print(liczby[0:3])
print(liczby[-3])
print(liczby)
# [54, 999, 34]
# 567
# [54, 999, 34, 666, 567, 999, 'A']

# rozpakowanie sekwencji
tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

# tworzymy krotkę z listy
krotka = tuple(lista_copy)
print(type(krotka))
print(krotka)
# <class 'tuple'>
# ('Adam', 'Anita', 'Ola', 'Radek')

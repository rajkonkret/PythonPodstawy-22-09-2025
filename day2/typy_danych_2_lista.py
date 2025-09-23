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

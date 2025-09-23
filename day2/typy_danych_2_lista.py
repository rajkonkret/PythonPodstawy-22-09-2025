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



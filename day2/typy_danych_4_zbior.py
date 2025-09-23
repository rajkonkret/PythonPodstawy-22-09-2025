# zbior (set) - przechowuje unikalne wartości (brak duplikatów)
# zbior nie zachowuje kolejności przy dodawaniu elemntów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie, zamiana na zbior
print(zbior)
print(type(zbior))
# {33, 66, 777, 11, 44, 22, 55}
# <class 'set'>

# pusty zbior
zb2 = set()  # tylko i wyłącznnie słówkiem set()
print(zb2)  # set() - pusty zbior
print(type(zb2))  # <class 'set'>

# dodanie eleemntów do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
zbior.add(33)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunie pierwszy element
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
zmienna = zbior.pop()
print("Zmienna:", zmienna)  # Zmienna: 66

zbior_copy = zbior.copy()  # kopia elementów zbioru
print(zbior)
print(zbior_copy)
print(id(zbior))
print(id(zbior_copy))
# 1721301683104
# 1721306862016


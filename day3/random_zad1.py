import random

# działania na liczbach losowych

"""Return random integer in range [a, b], including both end points.
       """
print(random.randint(1, 100))  # int, od 1 do 100
print(random.randrange(1, 100))  # 31, od 1 do 99
print(random.randrange(5))  # int 3, od 0 do 4

print(random.random())  # float, 0.703562155752746 od 0 do 0.9999999
print(random.random() * 7)  # float od 0 do 6.9999999

lista = [67, 45, 32, 68, 90, 42, 69]
print(random.choice(lista))  # 32, wylosowany element z listy

lista_kula = list(range(1, 50))
print(lista_kula)
wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)  # 39

print(random.choices(lista_kula, k=6))  # [29, 27, 38, 7, 38, 31], losuje z powtórzeniami
print(random.sample(lista_kula, 6))  # [26, 6, 22, 28, 23, 16], losowanie bez powtórzeń

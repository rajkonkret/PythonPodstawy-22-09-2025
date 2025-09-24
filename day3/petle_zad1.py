# pętla - pozwala wielokrotnie wykonać fragment kodu
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # niema zmienna
    print("Test podłoga")
    print(_)

for i in range(5):
    print(i + 2)
    print(i * 2)

#  przerobić na pętle lotto
lista_kula = list(range(1, 50))
lista_wyn = []
for _ in range(6):  # sześć razy
    wyn = random.choice(lista_kula)
    lista_kula.remove(wyn)
    print(wyn)  # 39
    lista_wyn.append(wyn)

print(lista_wyn)  # [49, 46, 11, 44, 43, 36]

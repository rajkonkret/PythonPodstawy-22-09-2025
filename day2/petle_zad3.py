# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat!")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(45 * "-")
print("Licznik:", licznik)  # Licznik: 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat3 !!!")

# password = input("Podaj hasło")
# while password != "secret":  # != różne
#     password = input("Podaj ponownie")
#
# print("Hasło prawidłowe")
# Podaj hasło234ewedd
# Podaj ponownieewrewrwe
# Podaj ponowniewerwerwe
# Podaj ponowniesdfsdfsd
# Podaj ponowniesecret
# Hasło prawidłowe

# lista = []
# lista_int = []
# while True:
#     wej = input("podaj liczbę:")  # -> str
#     # A string is numeric if all characters in the string are numeric
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))  # rzutujemy na inta
#
# print(lista)
# print(lista_int)
# podaj liczbę:1
# podaj liczbę:2
# podaj liczbę:3
# podaj liczbę:4
# podaj liczbę:5
# podaj liczbę:a
# ['1', '2', '3', '4', '5']
# podaj liczbę:1
# podaj liczbę:2
# podaj liczbę:3
# podaj liczbę:4
# podaj liczbę:5
# podaj liczbę:a
# ['1', '2', '3', '4', '5']
# [1, 2, 3, 4, 5]

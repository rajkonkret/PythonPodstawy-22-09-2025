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

password = input("Podaj hasło")
while password != "secret":  # != różne
    password = input("Podaj ponownie")

print("Hasło prawidłowe")
# Podaj hasło234ewedd
# Podaj ponownieewrewrwe
# Podaj ponowniewerwerwe
# Podaj ponowniesdfsdfsd
# Podaj ponowniesecret
# Hasło prawidłowe

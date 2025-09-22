import sys

wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)
# 2072
# -1978
# 95175
# 0.023209876543209877 -> int / int -> float

# 2025 // 47 = 43 całe
# 43 * 47 = 2021
# reszta = 2025 - 2021 = 4
print(rok // wiek)  # część całkowita dzielenia
print(rok % wiek)  # modulo, reszta z dzielenia
print(10 % 3)  # 1 reszty

print(wiek ** rok)

# len() - zwraca długość kolekcji
# print(len(wiek ** rok)) # TypeError: object of type 'int' has no len()
print(len(str(wiek ** rok)))  # str - zamiennia liczbę na tekst, długość 3386 znaków
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0



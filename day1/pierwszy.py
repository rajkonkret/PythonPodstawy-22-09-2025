import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 nie ma błędów
# PEP8  - zasadyformatowania kodu w Pythonie
# https://peps.python.org/pep-0008/
# ctrl alt l - formatowanie kodu
print("Radek")  # Radek
print("Radek")  # Radek
print("Radek")  # Radek
print("Radek")  # Radek
print("Radek")  # Radek
print("Radek")  # Radek
print("Radek")  # Radek
print("Radek")  # Radek
print("Radek")  # Radek
# ctrl d - powielanie linii
print('Radek')  # Radek
# ctrl / - szybkie komentowanie linii
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-22-09-2025\day1\pierwszy.py", line 17
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 17)
#
# Process finished with exit code 1
print("Kolejna komenda")

print("Radek \"Radek\"")  # \ - znak ucieczki
# Radek "Radek"

# type()
print(type("Radek"))  # <class 'str'>, tekst, string

print("39" + "39")  # 3939 łączy teksty, konkatenacja

print(39 + 39)  # 78
print(type(39))  # <class 'int'>, integer, liczby całkowite

print(sys.int_info)

# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
# print(39 + "39") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# musimy rzutowac typy, jeśli mamy typy mieszane
print(int("39"))  # rzutowanie, zamian ana int
print(39 + int("39"))  # 78

print(5 * "4")  # 44444
print(5 * 4)  # 20

# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'
print(int(168) + int("35"))  # 203

# zmienna - pudełko na dane
# snake_case
# nazwa zmiennej powinna podpowiadac co ma zawierac zmienna

# typowanie dynamiczne
# typ zmiennej jest określany na postawie danych jakie zawiera
name = "Radek"
print(name)  # wypisze wartość zmiennej, Radek
print(type(name))  # <class 'str'>

name = "Radek"
print(name + "Kowalski")  # RadekKowalski
# print(name + 90)  # TypeError: can only concatenate str (not "int") to str
name = 90
print(name)
print(type(name)) # <class 'int'>

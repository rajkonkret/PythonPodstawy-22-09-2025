# wyjątki - błedy w działaniu programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-22-09-2025\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("A" * "23")
    # int("A")
    # raise KeyError  # rzucenie konkretnego wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Błąd:", e)
else:  # tylko gdy nie ma błędu
    print('Wynik:', wynik)
finally:  # wykona się zawsze
    print("Kolejne obliczenie")

print("Dalsza częśc programu")
# Nie dziel przez zero
# Dalsza częśc programu
# Błąd typu
# Dalsza częśc programu
# Bład wartości
# Dalsza częśc programu
# Błąd:
# Dalsza częśc programu
# Wynik: 30.0
# Kolejne obliczenie
# Dalsza częśc programu
# Bład wartości
# Kolejne obliczenie
# Dalsza częśc programu

# try - except - [else - finally]

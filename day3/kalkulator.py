# napisać program kalkulator z wykorzystaniem pętli while True
# menu z dostępnymi opcjami
# ma mieć opcję wyjscia
# + - * /
# wyświetlić wynik w sposób sformatowany
# obsłużyć wyjątki

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj wybraną opcję")
    if odp == "5":
        break

    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        if odp == "1":
            print(f'Wynik {a} + {b} = {a + b}')
        elif odp == "2":
            print(f'Wynik {a} - {b} = {a - b}')
        elif odp == "3":
            print(f"Wynik {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Bład:", e)
    finally:
        print("Podaj kolejną operację")

wyr = "5*7+12"
print(eval(wyr))  # print(f'Wynik {a} + {b} = {a + b}')
a = 10
b = 30
dict1 = {"dodawanie": a + b}
print(dict1['dodawanie'])

# stworzyć funkcję obliczającą średnią

def srednia(name=None, *cyfry):
    print(cyfry)  # (1, 2, 3)
    count = len(cyfry)
    suma = 0
    sum_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = sum_p / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi: {avg}")
        print(f"Średnia dla ucznia {name} wynosi: {avg_p}")
    finally:
        print("Następny uczeń")


srednia(1, 2, 3)  # (1, 2, 3)
srednia()  # ()
# (1, 2, 3)
# Średnia wynosi: 2.0
# ()
# Bład: division by zero
srednia("Radek", 4, 5, 6, 7, 8, 9)
# (2, 3)
# Średnia dla ucznia 1 wynosi: 2.5
# Średnia dla ucznia 1 wynosi: 2.5
# Następny uczeń
# ()
# Bład: division by zero
# Następny uczeń
# (4, 5, 6, 7, 8, 9)
# Średnia dla ucznia Radek wynosi: 6.5
# Średnia dla ucznia Radek wynosi: 6.5
# Następny uczeń

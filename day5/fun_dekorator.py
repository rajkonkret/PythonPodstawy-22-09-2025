# dekorator
# funkcj, która jako argument przyjmuje inną funkcję
# wykorzystuje konstrukcje funkcji wew
def dekor(func):
    def wew():
        print("Dekorujemy")
        return func()  # musimy uruchomic funkcję dekorowaną

    return wew  # zwracamy adres funkcji wew


@dekor  # użycie naszego dekoratora
def hej():
    print("hej")


hej()


# hej - bez dekorator
# po dodaniu dekoratora:
# Dekorujemy
# hej

# dekorator, któy wynik działania funkcji zwraca dużymi literami
# funkcja zwraca str
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!"


print(greeting())  # Hello World!
# po dodaniu dekoratora
# HELLO WORLD!

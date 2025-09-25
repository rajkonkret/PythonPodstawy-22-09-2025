# funkcja wewnętrzna, zagnieżdżona
# dekorator - wykorzystuje zasady funkcji zagnieżdzonej

def fun1():
    print('To jest fun1')

    def fun2():
        print("To jest fun2")

    # fun2()
    return fun2  # zwracamy adres funkcji fun2, referencje


fun1()
print(fun1())  # <function fun1.<locals>.fun2 at 0x0000028AE355CEA0>
xfun = fun1()
print(xfun)  # <function fun1.<locals>.fun2 at 0x000001F9D591CEA0>
print(type(xfun))  # <class 'function'>
# () - uruchomią funkcje spod adresu jaki jest zawarty w zmiennej
xfun()  # To jest fun2

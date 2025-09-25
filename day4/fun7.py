def connect(**opcje):  # ** dowolna ilość argumentów nazwanych
    print(opcje)


connect()  # {}
connect(a=100)  # {'a': 100}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4, 5, 6, 7, 8, 9)  # (1, 2, 3, 4, 5, 6, 7, 8, 9) {}
all_args(a=10, b=23, c=90, name="Radek")  # () {'a': 10, 'b': 23, 'c': 90, 'name': 'Radek'}
all_args(1, 2, 3, 4, a=90, b=90, name="Radek")
# (1, 2, 3, 4) {'a': 90, 'b': 90, 'name': 'Radek'}

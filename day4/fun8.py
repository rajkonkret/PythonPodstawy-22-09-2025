def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)
# a=1, b=2
# c=42, d=256
all_params(1, 2, 3, 4)
# a=1, b=2
# c=3, d=4

# all_params(a=8, b=9, c=10, d=11)
# TypeError: all_params()
# got some positional-only arguments passed as keyword arguments: 'a, b'
# / oddziela argumenty pozycyjne od nazwanych
# a i b mogą byc tylko po nazwie przekazane
all_params(8, 9, c=10, d=11)
# a=8, b=9
# c=10, d=11

print(50 * "-")


def all_params2(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


all_params2(1, 2)
# a=1, b=2
all_params2(1, 2, c=3)
# a=1, b=2
# c=3, d=256
all_params2(1, 2, 3, 4, 5, 6, 7, 8, 8)
# a=1, b=2
# c=3, d=256
# args=(4, 5, 6, 7, 8, 8)
# kwargs={}
# d tylko i wyłacznie po nazwie bo jest po *args
all_params2(1, 2, 3, 4, 5, 6, 7, 8, 8, d=90)  # c=3, d=90
all_params2(1, 2, 3, 4, 5, 6, 7, 8, 8, d=90, name="Radek", e=900)  # kwargs={'name': 'Radek', 'e': 900}
all_params2(1, 2, 3, 4, 5, 6, 7, 8, 8, d=90, name="Radek", e=900, a=876)
# kwargs={'name': 'Radek', 'e': 900, 'a': 876}

def args_function(*args):
    pass


def kwargs_function(**kwargs):
    pass


def args_kwargs_function(*args, **kwargs):
    pass


def add(*args, **kwargs):
    s = 0
    for arg in args:
        s += arg
    for value in kwargs.values():
        s += value
    return s


print(add())
print(add(a=1))
print(add(a=1, d=2))
print(add(a=1, b=2, c=3))
print(add(1, 2, a=3, b=4))

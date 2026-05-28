def add(a, b):
    return a + b


class Person:
    pass


if __name__ == '__main__':
    x = add(1, 2)
    c = 7
    d = 10
    y = add(c, d)
    print(x, y)
    p = Person()
    print(p)
    print(type(p))

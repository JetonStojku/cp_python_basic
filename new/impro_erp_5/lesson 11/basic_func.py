class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def add(a, b):
    return a + b


if __name__ == '__main__':
    x = add(7, 5)
    print(x)
    y = add(3, 4)
    print(y)
    z = Number(2, 3)
    print(type(z))

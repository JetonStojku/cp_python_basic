def find_max(a, b):
    if a > b:
        print(True)
    else:
        print(False)


lst = [1, 2]
find_max(lst[0], lst[1])
find_max(*lst)

d = {'a': 10, 'b': 2}
find_max(d['a'], d['b'])
find_max(**d)

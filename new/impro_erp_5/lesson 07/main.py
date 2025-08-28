def hello(name, surname=''):
    # if surname:
    #     surname = f' {surname}'
    # print(f'Hello {name}{surname}!')

    if surname:
        print(f'Hello {name} {surname}!')
    else:
        print(f'Hello {name}!')


hello('filan', 'fisteku')
hello(surname='Smith', name='Tom')
hello('Anna')

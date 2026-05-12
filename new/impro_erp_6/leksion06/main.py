x = 50


def func():
    global x
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)


print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)

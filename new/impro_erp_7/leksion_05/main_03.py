"""U1"""
"""
Ndertoni nje funksion i cili merr nga perdoruesi sa
numra te vargut te fibonacit do te printoje dhe i 
printon ato.

fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, n):
            fib = a + b
            a = b
            b = fib
        return fib


print(fib(10))
print(fib(20))

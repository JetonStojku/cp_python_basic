"""U2"""
"""
Ndertoni nje program i cili merr nga perdoruesi sa
numra te vargut te fibonacit do te printoje dhe i 
printon ato.

fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""

n = int(input("Enter the sequences quantity: "))

if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    a = 1
    b = 1
    print(1, 1, end=' ')
    for i in range(2, n):
        fib = a + b
        print(fib, end=" ")
        a = b
        b = fib

        # b = a + b
        # a = b - a
        # a, b = b, a + b

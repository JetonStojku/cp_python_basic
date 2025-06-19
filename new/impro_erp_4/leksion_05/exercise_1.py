def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


print(is_perfect(8128))

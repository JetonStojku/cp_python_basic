def print_pascal(n):
    if n < 1:
        return []
    elif n == 1:
        return [[1]]
    else:
        lst = [[1]]
        for i in range(1, n):
            lst_2 = [1]
            for j in range(1, i):
                lst_2.append(lst[i - 1][j] + lst[i - 1][j - 1])
            lst_2.append(1)
            lst.append(lst_2)
        return lst


pascal = print_pascal(7)
print(pascal)

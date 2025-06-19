""" U 5.3 """
"""
Build a function that takes two numbers from the user and returns the multiplication table in the following format:

```
Example: 3, 4

|   |1  |2  |3  |4  |
|1  |1  |2  |3  |4  |
|2  |2  |4  |6  |8  |
|3  |3  |6  |9  |12 |
```

3 * 4
12
"""


def print_tabel(n, m):
    print(f'|\t', end='')
    for i in range(1, m + 1):
        print(f'|{i}\t', end='')
    print('|')
    for i in range(1, n + 1):
        print(f'|{i}\t', end='')
        for j in range(1, m + 1):
            print(f'|{i * j}\t', end='')
        print('|')


print_tabel(3, 4)

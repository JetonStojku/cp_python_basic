lst = [7, 10, 12, 14, 21, 32, 1]

x = dict()
print(x)
for i in filter(lambda x: x % 7 == 0, lst):
    print(i)

y = list(range(1, 11))
print(y)
# for i in range(1, 11):
#     print(i)

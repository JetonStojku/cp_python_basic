# import basic_func
# import basic_func as m
# from basic_func import *
# from basic_func import add as sum
from basic_func import add, Number

x = 5
y = 23

# s = basic_func.add(x, y)
# s = m.add(x, y)
s = add(x, y)
# s = sum(x, y)
# s = add(x, y)

print(s)

a = Number(7, 8)
print(type(a))

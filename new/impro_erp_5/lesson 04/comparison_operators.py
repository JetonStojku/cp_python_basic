a = 'hi' == 'hi '
print(a)

a = True
print(not a)
print('-' * 40)
a1 = 10
a2 = 10
if a1 <= a2:
    print('a1<a2')
elif a1 == a2:
    print('a1=a2')
else:
    print('a1>a2')

print('end!')

c = False  # 0, '', None, [], {}, (), set()
if c:
    print('hello')
else:
    print('Goodbye')

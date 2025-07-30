s1 = 'Hello World!'

print(s1)
print(s1[-2])

l = len(s1)
print(l)

print(s1[2:11:3])
print(s1[2:11])
print(s1[10:1:-1])
print(s1[::-1])

s2 = 'Hello'
s3 = 'World'
s4 = s2 + ' ' + s3
print(s4)

n1 = '10'
n2 = '20'
s5 = n1 + n2
print(s5)

n3 = 3
s6 = 'Hello'
s7 = s6 * n3
print(s7)

s8 = 'hello world'
print(s8.upper())
print(s8.lower())
print(s8.title())
print(s8.split())
print(s8.split('o'))
print(s8.split('l'))
print(s8.split('z'))
print(s8.split('or'))
print(s8.split('os'))

name = input('Enter your name: ')
surname = input('Enter your surname: ')

hello = 'Hello {}!'.format(name)
print(hello)

hello = 'Hello {} {}!'.format(name, surname)
print(hello)

hello = 'Hello {1} {0}!'.format(name, surname)
print(hello)

hello = 'Hello {1} {0} {1}!'.format(name, surname)
print(hello)

hello = f'Hello {name} {surname}!'
print(hello)

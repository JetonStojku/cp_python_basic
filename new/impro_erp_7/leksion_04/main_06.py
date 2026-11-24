i = 0
while i < 5:
    i += 1
    print(i)

print("End 1", "-" * 28)

i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

print("End 2", "-" * 28)

i = 0
while i <= 20:
    i += 1
    if i % 3 == 0:
        continue
    print(i)

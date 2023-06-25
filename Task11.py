n = int(input('Введите число: '))
a0 = 0
a1 = 0
a2 = 1
i = 2
while a0 < n:
    a0 = a1 + a2
    a1 = a2
    a2 = a0
    i += 1
    if a0 > n:
        i = 0
if i != 0:
    print(i)
else:
    print(-1)
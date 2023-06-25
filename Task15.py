n = int(input('Введите количество арбузов: '))
x = int(input('Введите массу арбуза: '))
min_massa, max_massa = x, x
for i in range(n - 1):
    x = int(input('Введите массу арбуза: '))
    if max_massa < x:
        max_massa = x
    elif min_massa > x:
        min_massa = x
print(min_massa, max_massa)
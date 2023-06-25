print('Введите целое положительное число:')
n = int(input())
i = 2
result = 1

while i <= n:
    result *= i
    i += 1
print(f'{n}! = {result}') 
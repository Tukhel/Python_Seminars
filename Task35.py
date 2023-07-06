# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

n = int(input('Введите число: '))
f = 1
for i in range(2, n // 2 + 1):
    if n % i == 0:
        f = 0

if f == 0:
    print('no')
else:
    print('yes')
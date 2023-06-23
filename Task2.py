# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('Введите трех значное число:')
number = int(input())

if number < 100 or number > 999:
    print('Введено не корректное число')
else:
    sum = number % 10
    number //= 10
    sum += number % 10 + number // 10
    print(sum)
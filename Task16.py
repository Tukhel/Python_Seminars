# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint as rd


numbers = int(input("Введите кол-во элементов массива: "))
array = []
for i in range(numbers):
    array.append(rd(1, 21))
print(array)

digit = int(input("Введите искомое число: "))
count = 0
for i in range(len(array)):
    if digit == array[i]:
        count += 1
print(count)
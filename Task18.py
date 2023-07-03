# Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint as rd


numbers = int(input("Введите кол-во элементов массива: "))
array = []
for i in range(numbers):
    array.append(rd(1, 21))
print(array)

digit = int(input("Введите число для сравнения: "))
temp = array[0]
for i in range(1, len(array)):
    if temp == digit:
        break
    elif array[i] > temp and array[i] < digit:
        temp = array[i]
print(temp)
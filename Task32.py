# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

list_1 = [int(i) for i in input('Введите элементы массива: ').split()]
min = int(input('Введите минимальное значение диапозона: '))
max = int(input('Введите максимальное значение диапозона: '))

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')

# С помощью списка
# list_2 = []
# for i in range(len(list_1)):
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(list_2)
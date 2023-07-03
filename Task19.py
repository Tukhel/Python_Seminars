# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
from random import randint as rd


n = int(input('Введите количество элементов: '))
numbers = list()
for i in range(n):
    numbers.append(rd(1, 51))
print(numbers)
k = int(input('Введите количество сдвигов: '))
k = k % n

result = [0] * n
for i in range(k):
    result[i] = numbers[n - k + i]
for i in range(n - k):
    result[k + i] = numbers[i]
print(result)
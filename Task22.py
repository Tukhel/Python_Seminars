# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = (int(input("Введите количество элемментов N множества: ")))
m = (int(input("Введите количество элемментов M множества: ")))
list_n = []
list_m = []
for i in range(n):
    list_n.append(int(input("Введите элемент множества N: ")))
print(list_n)
for i in range(m):
    list_m.append(int(input("Введите элемент множества M: ")))
print(list_m)
total = set()
print(f"Объединение двух множеств: {total.union(list_n, list_m)}")
# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random

# number = int(input("Введите количество элементов массива: "))
# array = [random.randint(0, 10) for _ in range(number)]
# print(f"Исходный массив чисел : {array}" )
# sum = 0
# for i in range(1, len(array), 2):
#     sum = sum + array[i]
    
# print(f"Сумма элементов на нечётной позиции = {sum}")


import random

number = int(input("Введите количество элементов массива: "))
array = [random.randint(0, 10) for _ in range(number)]
print(f"Исходный массив чисел : {array}" )
new_array = sum(filter(lambda x: array.index(x) % 2 != 0, array))
print(f"Сумма элементов на нечётной позиции = {new_array}")


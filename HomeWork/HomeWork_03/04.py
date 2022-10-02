from decimal import Decimal

# result = [float(Decimal(i) / 100) for i in range(-100, 101)]

# print(result)


import random

number = float(input("Введите количество элементов массива: "))
array = [float(Decimal(i) / 100) for _ in range(number)]
print(f"Исходный массив чисел : {array}" )
sum = 0
for i in range(1, len(array), 2):
    sum = sum + array[i]
    
print(f"Сумма элементов на нечётной позиции = {sum}")
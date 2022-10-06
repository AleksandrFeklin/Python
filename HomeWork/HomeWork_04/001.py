# 1 .  Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import random

a = random.uniform(0.0, 100.0)
print(f"Заданное число: {a}")
acc = input("задайте точность: ")
print(round(a, len(acc) - 2))


#  2 .Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
exit()

n = int(input("Введите N: "))
lst = []
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
lst2 = []

for i in range(0, len(lst)):
    if n % lst[i] == 0:
        lst2.append(lst[i])
print(f"Список натуральных множителей {lst2}")

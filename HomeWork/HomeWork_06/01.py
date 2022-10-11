# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# number = int(input('Введите день недели: '))
# if number == 6 or number == 7:
#     print('Выходной')
# else:
#     print('Будний')
    
day = int(input("Введите Введите день недели: "))  
week = (lambda day: "Выходной" if (day == (6 or 7)) else "Будний день")
print(week (day))

# # Напишите программу, которая
# # принимает на вход число N
# # и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
# factorial = 1
# list = []
# for i in range(1, n + 1):
#     factorial *= i
#     list.append(factorial)
# print(f"Набор произведений чисел = {list}" )

import math
number = int(input("Введите число: "))
factorial = list(map(lambda f:math.factorial(f), range(1,number+1)))
print(f"Набор произведений чисел = {factorial}" )


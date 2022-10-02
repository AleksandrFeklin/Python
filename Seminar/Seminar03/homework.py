# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11
# number = input("Введите вещественное число :")
# summa = 0
# for i in number:
#     if i.isdigit():
#         summa += int(i)
# print(summa)

# number = float(input("Введите вещественное число :"))
# summa = 0
# number = abs(number)


# def digit_after_dot_counter(num: float):
#     count = 0
#     div = 1
#     while True:
#         if not (num * div == int(num * div)):
#             count += 1
#             div *= 10
#         else:
#             break
#     return count

# print(digit_after_dot_counter(number))  # кол-во знаков после запятой

# num = number * (10 ** digit_after_dot_counter(number))
# print(num)

# while num != 0:
#     summa += num % 10
#     num //= 10
# print(int(summa))


# # Напишите программу, которая
# # принимает на вход число N
# # и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input("Введите число : "))
# def factorial(number):
#     listNum = []
#     factorial = 1
#     for i in range (1 , number+1):
#        listNum.append(i * factorial)
#        factorial *=i
#     return listNum
# print(factorial(number))


# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# number = int(input("Введите число : "))
# def ArrayDigits(number):
#     listNum = []
#     for i in range (1 , number+1):
#        listNum.append((1+1/i)** i)
#     return listNum
# print(ArrayDigits(number))
# print(sum(ArrayDigits(number)))

# Реализуйте алгоритм перемешивания списка.

from random import random, randrange


list = [1,2,3,4,5,66,678]
list_shuffled = []
for i in range(0, len(list)):
    j = randrange(0, len(list))
    list_shuffled.append(list[j])
    list.remove(list[j])
print(list_shuffled)




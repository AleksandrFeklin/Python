# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11

# number = (input('Введите число: '))
# summ = 0
# for i in range(len(number)):
#     if number[i].isalnum() == True:
#         summ += int(number[i])
# print(f"Сумма чисел = {summ}")


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


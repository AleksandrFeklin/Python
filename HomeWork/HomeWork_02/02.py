# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

number = int(input("Введите число: "))
a = 0
list = []
for i in range(1, number + 1):
    a = round((1 + (1 / i)) ** i, 2)
    list.append(a)
print(f"Cписок чисел : {list}")
print(f"Сумма чисел = {sum(list)}")


# Реализуйте алгоритм перемешивания списка.
import random
list_numbers = list(range(0,9))
print(f" Исходный массив : {list_numbers}")
random.shuffle(list_numbers)
print(f" Перемешанный массив : {list_numbers}")
# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

first_list = [float(i)  for i in input('Введите вещественные числа через пробел: ').split()]
second_list = [round(i % 1, 2) 
               for i in first_list if i % 1 != 0]
print(f'Разница между max и min значением дробной части элементов = {max(second_list) - min(second_list)}')




# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
#     print(f"Число {num} в двоичной системе это {binum})

exit()



number = int(input('Введите  Нумбер: '))
def bi_number(num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    return result
print(f'Нумбер "{number}" в Двоичной системе счисления = {bi_number(number)}')
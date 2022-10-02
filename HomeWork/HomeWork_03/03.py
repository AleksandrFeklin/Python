# 5. Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21][Негафибоначчи]

number = int(input('Задайте размер списка : '))
def fibonacci (num):
    fibb = []
    n1 = n2 = 1
    for i in range(num):
        fibb.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for i in range(num+1):
        fibb.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fibb
print(f"Готовый список : {fibonacci(number)}")
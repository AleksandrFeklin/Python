# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел..
# n = int(input('Введите число 1: '))
# m = int(input('Введите число 2: '))

# k = min(n,m)
# s = max(n,m)
# i=1
# while (k*i)%s != 0:
#   i+=1
# print(k*i)

# n = int(input("Введите число 1: "))
# m = int(input("Введите число 2: "))
# i = 1
# while (min(m, n) * i) % max(m, n) != 0:
#     i += 1
# print(f"Минимальное общее кратное для {n} и {m} = {min(m,n)* i}")


# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;



# # s = input(1-2*3)
# # print(eval(s)) 

# str = '1-2*3'
# sum = 0
# for i in range(len(str)):
#     if str[i] == '*':
#        sum =  int(str[i-1])* int(str[i+1])
#     for i in 
#     elif str[i] == '-':
#         print(int(str[i-1])-sum)
        
        
# myList = ['3' ,'8', '4', '6']        
# print(myList)
# myList = list(map(int,myList))
# print(myList)

# myList = ['3' ,'8', '4', '6']        
# print(myList)
# # myList = list(map(int,myList))
# myList = list(map(lambda x : int (x)  + 1 ,myList))
# print(myList)
# from random import randint, random
# myList = [str(randint(0,10)) for i in range(int(input("Размер : "))) ]
# print(myList)
from random import randint, random


myList =[randint(0,10) for _ in range(10)]
print(myList)


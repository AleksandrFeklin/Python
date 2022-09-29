from importlib.resources import path
from typing import Concatenate
## ФАЙЛЫ
# Как работать с файлами:
# Cвязать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных
# r - открытие для чтения данных
# w -открытие для записи данных
# W+, r+


#№Функции и методы

# with open("file.txt", "a") as data:
#     data.write("line 111\n")
#     data.write("line 2312\n")

# colors = ['red', 'green','blue111']
# data = open('file.txt', 'a')
# #data.writelines(colors)    #разделителей не будет\
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close


# exit()
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()


## Функции
##Это фрамент программы , используемый многократно

#def function_name(x) :
    #body line 1
    # ....
    # body line n
    # optional return


# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# import hello as h
# print(h.f(1))      


# def new_string(symbol, count ) :
#     return symbol * count

# print(new_string('!', 5))     # !!!!!
# print(new_string('!'))        # TypeError missing 1 required...    

# def new_string(symbol, count = 3 ) :
#     return symbol * count

# print(new_string('!', 5))     # !!!!!
# print(new_string('!'))        # !!!
# print(new_string('4'))        # 12


# def concatenatio(*params) :
#     # res :  str = ""   # строка
#     res :  int = 0     # Числа

#     for item in params :
#         res += item
#     return res  

# # print(concatenatio('a', 's', 'd' , 'w'))     #asdw
# # print(concatenatio('a', '1', 'd' , '2'))     #a1d2
# print(concatenatio(1, 2, 3 , 4))     #TypeError ....

## РЕКУРСИЯ

def fib(n) :
    if n in [1,2] :
        return 1
    else :
        return fib(n - 1) + fib (n -2)
list = []
for e in range(1,10) :
    list.append(fib(e))
print(list)   #  1 1 2 3 5 8 13 21 34            

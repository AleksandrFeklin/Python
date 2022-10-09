# 1. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# from random import randint, shuffle
# from random import randint as rI

# string = "аваа выва ыыа выа аюыва выаа ыа"
# print(string)

# elem = input("Введите элемент :")
from turtle import position

position = []
for i in range(1, 10):
    position.append(i)
sign = "0"    
while True:
    if sign =="0":
       sign = "X"
    else:
        sign = "0"    
    # position[4]  = "0"
    # position[8]  = "0"
    print(f"{position[0]:^5}|{position[1]:^5}|{position[2]:^5}")
    print("---------------")
    print(f"{position[3]:^5}|{position[4]:^5}|{position[5]:^5}")
    print("---------------")
    print(f"{position[6]:^5}|{position[7]:^5}|{position[8]:^5}")

    index = int(input(f"\n\nXод {'Игрока' if sign == 'X' else 'Противника'}: "))
    position[index - 1] = sign


exit()
import random

# from turtle import distance


listInt = list([i for i in range(10)])

random.shuffle(listInt)
print(listInt)
distance = []
new = []
for i in range(0, len(listInt) - 1):
    sub = []
    sub.append(listInt[i])
    while True:
        # sub= []
        # sub.append(listInt[i])
        # for k in (i+1, len(listInt)-1):
        if listInt[i] < listInt[i + 1]:
            sub.append(listInt[i + 1])
            i += 1
        else:
            break
        # if listInt[i+1] <listInt[i+2]:
        #     sub.append(listInt[i+1])
    distance.append(sub)
# print(distance)
for i in range(len(distance)):
    if len(distance[i]) != 1:
        new.append(distance[i])
print(new)

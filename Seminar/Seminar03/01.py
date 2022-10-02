# Задайте список.Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число

# my_list = ["sa12", "sads", "21d2", "s12", "fd12"]
# trigger = False
# for i in  range (len(my_list)):
#     if my_list[i].find("3") >= 0:
#        trigger = True
#     break
# if trigger: print("Число присутствует")
# else: print("Число отсутвует")


# string = ["sa12", "sads", "21d2", "s1ddsf", "fd12"]
# num = input("Введите число : ")
# for element in string:
#     if num in element:
#        print("Присутствует")
#        #break
#     else:
#        print("Отсутствует")
#        #break

# string = 's13da32'
# for i in string :
#     print(i.isdigit())

# Напишите программу, которая определит позицию второго вхождения строки
# в списке либо соообщит , что её нет


# list = ["sagfg", "sagfg", "sagfg", "sddsf", "sagf"]
# count = 0
# findWord = "sagfg"
# for i in range(len(list)):
#     if list[i] == (findWord):
#         count += 1
#         if count == 2:
#            print(i)
#            break
# else:
#     print("Error")


from random import randint
from time import time, time_ns


def randomize(min, max):
    num = time_ns()/ 2  # * 100000
    print(num)
    # while num > max:
    #     num //= max
    return int(num % max)


print(randomize(1, 10))
print(randint(0, 100))
print(randint(0, 100))



# def random(min,max,random = 1) :
#     rnd = min
#     num = time() * 100000000000000000 % 100000000000000000
#     num /= random
#     print(num)
#     while num > max:
#         num //= max
#     rnd = rnd + num %10
#     return num
# print (random(1,100, random(1,100)))        
# print (random(1,100))  
# print (random(1,100))  
# 3 .  Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще каким-нибудь способом кроме множества
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

listt = input(("Введите элементы массива через пробел:")).split(" ")
list_int = [int(item) for item in listt]
print(f"Заданный список: {list_int}")


def repeat(list):
    listt2 = []
    for i in range(0, len(list)):
        count = 0
        for k in range(0, len(list)):
            if i != k and list[i] == list[k]:
                count += 1
        if count == 0:
            listt2.append(list[i])
    print(f"Не повторяющиеся элементы: {listt2}")


repeat(list_int)


# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


exit()


import random

k = int(input("Введите k: "))


def randomlist(k):
    list = []
    for i in range(0, k + 1):
        list.append(str(random.randint(0, 100)))
    return list


def ffunc(k, list):
    str_p = ""
    for i in range(k, -1, -1):
        if i != 0:
            if i != 1:
                if list[i] != 0 and list[i] != 1:
                    str_p += f"{list[i]}*x^{i} + "
                elif list[i] == 1:
                    str_p += f"x^{i} + "
                else:
                    str_p += ""
            if i == 1:
                if list[i] != 0 and list[i] != 1:
                    str_p += f"{list[i]}*x + "
                elif list[i] == 1:
                    str_p += f"x + "
                else:
                    str_p += ""
        else:
            if list[i] != 0:
                str_p += f"{list[i]} = 0"
            else:
                print(len(str_p))
                str_p = str_p[: len(str_p) - 2]
                str_p += f"= 0"
    return str_p


list1 = randomlist(k)
list2 = randomlist(k)
ffunc(k, list1)
print(ffunc(k, list1))
ffunc(k, list2)
print(ffunc(k, list2))


f1 = open("les4_1.txt", "w")
f1.write(ffunc(k, list1))
f1.close()

f2 = open("les4_2.txt", "w")
f2.write(ffunc(k, list2))
f2.close()

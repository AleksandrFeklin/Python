# # 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# # Пример: Для N = 5: 1, -3, 9, -27, 81

# Number = int(input('Введите число N : '))
# result = []
# for degree in range(Number):
#     result.append(str((-3) ** degree))
# print(" , ".join(result), end=".")

# # 2 . Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Number = int(input("Введите число N : "))
# dict = {}
# for key in range(1, Number + 1):
#     dict[key] = key * 3 + 1
# # result[5]     = 999
# print(dict)

# # 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.


textFirst = input("Введите первую строку: ")
textSecond = input("Введите вторую строку: ")
string = ""
subString = ""
if len(textFirst) > len(textSecond):
    string = textFirst
    subString = textSecond
else:
    string = textSecond
    subString = textFirst
print(string.count(subString))
count = 0
counter = 0
for i in range(len(string) - len(subString)):
    if string[i] == subString[0]:
        counterIn = 0
        for k in range(len(subString)):
            if subString[0 + k] == string[i + k]:
                counterIn += 1
        if counterIn == len(subString):
            counter += 1
print(f"Counter = {counter}")

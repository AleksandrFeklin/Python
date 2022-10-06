# from csv import list_dialects
# from random import randint, random

# myList = []
# def fillArray():
#     myList = []
#     for i in range(10):
#         myList.append(randint(-10, 10))
#     return myList
# new = fillArray()
# print(new)
# new.reverse()
# print(new)

# Считайте из файла список чисел. Напишите программу, которая найдет большее и меньшее число
# И запишет их в отдельный файл.
# В качестве символа-разделителя используйте пробел.
# data = open("fiLe.txt", "r")
# file = data.read().split(" ")
# data.close()
# print(file)
# for i in range(len(file)):
#     if file[i].isdigit:
#         file[i] = int(file[i])
# print(file)
# k = min(file)
# print(k)
# l=max(file)
# print(l)
# data = open("fiLe1.txt", "w")
# data.write(f'{k}\n')
# data.write(f'{l}\n')
# data.close()

pathRead = r"file.txt"
pathWrite = r"file1.txt"

try:
    with open(pathRead) as data:
        file = data.read().split(" ")
        print(file)
except:
    print("Файл не найден")
listInt = []
for elem in file:
    if elem.isdigit():
        listInt.append(int(elem))
try:
    with open(pathWrite, "w") as data:
        data.write(str(min(listInt)))
        data.write("\n")
        data.write(str(max(listInt)))
except:
    print("Ошибка работы с файлом")

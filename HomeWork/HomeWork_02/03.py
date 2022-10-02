# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from operator import pos
from random import randint, random
from turtle import position


number = int(input("Введите число : "))
listInt = []
for i in range(number):
    listInt.append(randint(-number, number))
print(listInt)

position = ""
with open("file.txt", "r") as data:
    position = data.read().split("\n")
print(
    f"Произведение  {int(position[0])} и {int(position[1])}"
    + f" элементов = {listInt[int(position[0])] * listInt[int(position[1])]}"
)

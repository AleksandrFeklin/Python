""" Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
Примеры:
- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90 """

# numbers = []
# for _ in range(5):
#     n = int(input('Введите число: '))
#     numbers.append(n)
# print(max(numbers))


# def ismax(a, b, c, d, e):

#     result = max(a, b, c, d, e)
#     print(result)

# ismax(6, 2, 3, 4, 5)


# maxx = int(input('Введите число: '))
# for _ in range(4):
#     n = int(input('Введите число: '))
#     if n > maxx:
#         maxx = n
# print(maxx)


# list = ['-1', '2', '3', '2', '0']
# print(list)
# for i in range(len(list)):
#     max = list[i]
#     if [i] > max:
#         max = [i]
# print(max)

# list = []
# for i in range(5):
#     list.append(int(input("Введите число : ")))
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)

# list = [54, 89, 908, 0, 789]
# print(list)
# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)


num_array = []
for i in range(5):
    num_array.append(int(input(f"Введите {i+1} число : ")))
for elem in range (len(num_array)):
    # print (f" Элемент {num_array[elem]} имеет индекс {elem}" )
    print (f"Максиимальное число в массиве - {max} " )




# Анонимные, lambda функции
# К чему это всё?
# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# from importlib.resources import path


# path = "/Users/Александр/Documents/project/python/lesson4.txt"
# f = open(path, "r")
# data = f.read() + " "
# f.close()

# numbers = []

# while data != "":
#     space_pos = data.index(" ")
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1 :]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)


# def select(f, col):
#     return [f(x) for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = "1 2 3 5 8 15 23 38".split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)


# Функция ﬁlter
# Функция ﬁlter() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с теми объектами, для которых функция вернула True.
# f(x) ⇒ x - чётное
# filter(f, [ 1, 2, 3, 4,5])
#                 ↓
#             [	2,	4 ]

# Нельзя пройтись дважды

# from unittest import result


# data = [x for x in range(10)]

# res = list(filter(lambda x: not  x % 2 , data))
# print(res)

data = "1 2 3 5 8 15 23 38".split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)

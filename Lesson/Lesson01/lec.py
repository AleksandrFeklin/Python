# print('hello world')

# # типы данных и переменная
# # 1) int  2) float 3) boolean 4) str 5) list 6) None

# value = None
# a = 123  # int
# b = 1.23  # float (числа с плавающей запятой)
# print(type(a))
# print(type(b))
# value = 1234
# print(type(value))
# s = 'hello world'  # "\n" вывод с новой строки
# print(s)  # вывод строки

# print(a, '-', b, s)  # 1 вариант вывода
# print('{} - {} - {}'.format(a, b, s))  # 2 вар-т вывода
# print('{1} - {2} - {0}'.format(a, b, s))  # 2.1 вар-т вывода
# print(f'{a} - {b} - {s}')  # 3 вар-т вывода

# f = False
# print(f)


# # массивы
list = [1, 2, 3, 4]
print(list)
list = ['1', '2', '3', 'hello']
print(list)

list = ['1', '2', '3']
col = ['hello', 1, 2, 4, 5, True]
print(list)
print(col)

# # ввод и вывод данных
# # print() - вывод данных
# # input() - ввод данных

print('Введите а')
a = input()
print('Введите b')
b = input()
print(a, b)  # 1 вар-т
print('{} {}'.format(a, b))  # 2 вар-т
print(f'{a} {b}')  # 3 вар-т

# # сумма двух строк
print('Введите а')
a = input()
print('Введите b')
b = input()
print(a, '+', b, '=', a+b)

# сумма двух целых чисел

print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
print(a, '+', b, '=', a+b)

# сумма двух нецелых чисел

print('Введите а')
a = float(input())
print('Введите b')
b = float(input())
print(a, '+', b, '=', a+b)


# # Арифметические операции
# # + сложение, - вычитание, * умножение, / деление с остатком, % остаток от деления,
# #  // деление без остатка, ** возведение в степень
# # Приоритет операций
# # **, ⊕ унарный плюс, ⊖ унарный минус, *, /, //, %, +, -
# # ( ) Скобки меняют приоритет

a = 123
b = 321
c = a + b
print(c)

a = 1.3
b = 3
c = round(a * b, 5) # round округление
print(c)

a = 3
a += 5
print(a)

# # Логические операции
# # >, >=, <, <=, ==, !=
# # not, and, or – не путать с &, |,^
# # Кое-что ещё: is, is not, in, not in

# a = 1 > 4 and 5 > 2
# print(a)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)

# is_odd = not f[0] % 2
# print(is_odd)

# # Управляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)
#     # Управляющие конструкции: if-else

# username = input('Введите имя: ')
# if username == 'Саша':
#     print('Ура, это же , САША!')
# elif username == 'Олег':
#     print('Я так ждала Вас, Олег!')
# elif username == 'Андрей':
#     print('Андрей - Loser')
# else:
#     print('Привет, ', username)

# # Управляющие конструкции: while, while-else

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# # while-else

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит))')
# print(inverted)

# # Управляющие конструкции: for

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 10, 5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# # О СТРОКАХ

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))                 # 39
# print('ещё' in text)             # True
# print(text.isdigit())            # False
# print(text.islower())            # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                         # c
# print(text[1])                         # ъ
# print(text[len(text)-1])               # к
# print(text[-5])                        # б
# print(text[:])                         # print(text)
# print(text[:2])                        # съ
# print(text[len(text)-2:])              # ок
# print(text[2:9])                       # ешь ещё
# print(text[6:-18])                     # ещё этих мягких
# print(text[0:len(text):6])             # сеикакл
# print(text[::6])                       # сеикакл
# text = text[2:9] + text[-5] + text[:2] #

# help(int)

# # Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran) # приведение типа рэндж к типу лист
# print(type(numbers))

# print(numbers)   # [1, 2, 3, 4, 5]
# numbers [0] = 10
# print(f'{len(numbers)} len')
# print(numbers)    # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)      # [20, 4, 6, 8, 10]
# print(numbers)    # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# # Функции

# def function_name(x):
#     body line 1
#     . . .
#     body line n
#     optional return

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))
# print(type(f(arg)))

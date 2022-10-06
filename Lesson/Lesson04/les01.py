# Анонимные, lambda функции
# def	sum(x): return x+10
# def	sum1(x): return x+22
# def	sum3(x): return x+242
# def	mult(x): return x**2
# def	mult2(x): return x**3
# def	mult4(x): return x**5
# sum(mult(2))
# sum1(mult2(2))
# def f(x):
#     x**2
# g = f
# print(f(1))
# print(g(1))


# def f(x):
#     return x**2
# g=f
# print(type(f))
# print(type(g))
# print(f(4))
# print(f(4))

# def calc1(x):
#     return x+10
# #print(calc1(10))
# def calc2(x):
#     return x*10
# #print(calc2(10))

# def math(op, x):
#     print(op(x))
# math(calc2, 10)
# math(calc1, 10)


# def sum(x,y):
#     return x+y

# f= sum
# def mylt(x,y):
#     return x*y
# def calc(op,a,b):
#     print(op(a,b))
#     # return op(a,b)

# calc(f, 4,5)

# def sum(x,y):
#     return x+y

# def mylt(x,y):
#     return x*y
# def calc(op,a,b):
#     print(op(a,b))
#     # return op(a,b)

# calc(lambda x, y: x+y, 4,5)


# # List Comprehension

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# # list = []
# # for i in range(1,101):
# #     if(i%2 ==0):
# #         list.append(i);
# # print(list)
# def f(x):
#     return x**3
# list =  [(i,f(i)) for i in range(1,21) if i %2 ==0]
# # list =  [f(i) for i in range(1,21) if i %2 ==0]
# # list = [(i,i) for i in range(1,21) if i %2 ==0]
# print(list)


## Функция map
# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта
# и возвращает итератор с новыми объектами.
# f(x) ⇒ x + 10

# map(f, [ 1,	2,	3,	4,	5])
#          ↓	↓	↓	↓	↓
#        [ 11,	12,	13,	14,	15]

# Нельзя пройтись дважды

# li = [x for x in range(1,20)]
# li = list(map(lambda x : x +10, li))
# print(li)

# data = list(map(int,'1 2 3'.split ()))
# for e in data:
#     print(e)
# print('--')
# for e in data:
#     print(e)


# def where(f, col):
#     return [x for x in col if f(x)]


# data = "1 2 3 5 8 15 23 38".split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

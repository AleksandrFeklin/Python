# a = 4
# b = a
# a += 5
# print(b)   #вывод 4


# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)    #1,2,3,4
# # c = a.copy()
# c = a[:]
# a.append(5)
# c.append(7)
# print(a)
# print(b)
# print(c)

# match case
a = 4
match a:
    case 1:
        print("Единица")
    case 2:
        print("Двойка")
    case 3:
        print("Тройка")
    case _:
        print("Не единица, не двойка и не тройка")

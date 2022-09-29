## КОРТЕЖИ
# Кортеж - это неизменяемый "список"

# t = ()
# print(type(t))   # tuple
# t = (1,)
# print(type(t))   # tuple
# t = (1)
# print(type(t))   # int
# t = (28, 9, 1990)
# print(type(t))    # tuple
# colors = ['red', 'green', 'blue']
# print(colors)     #['red', 'green', 'blue']
# t = tuple(colors)
# print(t)          #('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0])    # red
# print(t[2])    # red
# print(t[10])     # IndexError : tuple index out of range
# print(t[-2])     #green
# #print(t[-200])  # IndexError : tuple index out of range

# for e in t :
#     print(e)   # red green blue

# t[0] = 'black'  # TypeError : 'tuple' object does not support
# item assignment
# t = tuple(["red", "green", "blue"])
# red, green, blue = t
# print("r :{} g :{} ".format(red, green, blue))
# # r :red g: green b:blue


# a = (3,1, 41, 4)
# print(a)
# print(a[-2])
# # a[0] = 12  # Error
# a = (3, 4, 5)
# for item in a:
#     print(item)

## СЛОВАРИ
# Неупорядоченные коллекции произвольных объектов с доступом по ключу
dictionary = {}
dictionary =  \
    {"up": "↑",
     "left": "←",
      "down": "↓",
       "right": "→"
    }
print(dictionary["up"])
dictionary["up"] = "up"
print(dictionary["up"])

# print(dictionary)    #  { 'up' : ' ↑'  ......}
# print(dictionary['left'])  #
# типы ключей могут отличаться

# print(dictionary['up'])   #  ↑
# dictionary['left'] = '←'     
# print(dictionary['left'])    # ←
# print(dictionary['type'])   # KeyError: 'type'
# del dictionary['left'] #удаление элемента

# for item in dictionary :  #for (k,v) in dictionary.items():
#     print('{}: {}' .format(item, dictionary[item]))
# # up :   ↑
# # down :  ↓ 
# # right: →

# for k in dictionary.values():  # dictionary.values()  keys()
#     print(k)




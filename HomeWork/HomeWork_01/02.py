
# Напишите программу, которая 
# по заданному номеру четверти, 
# показывает диапазон возможных 
# координат точек в этой четверти (x и y).
n = int (input ('Введите номер четверти: '))
print ("Диапазон возможных координат точек в этой четверти:") 
if n ==1: 
    print ("х от 0 до +∞, y от 0 до +∞") 
elif n ==2: 
    print ("х от 0 до -∞, y от 0 до +∞") 
elif n ==3: 
    print ("х от 0 до -∞, y от 0 до -∞") 
elif n ==4: 
    print ("х от 0 до +∞, y от 0 до -∞")
else:
    print ("Вы задали значение, которое не является номером четверти")
from operator import eq
from random import randint as rI


def createEquation():
    degree = int(input("Введите максимальную степень многочлена : "))

    equation = ""
    for d in range(degree, -1, -1):
        coef = rI(-20, 20)
        # print(coef)
        if d == degree:
            if coef > 0:
                equation += str(coef) + "x^" + str(d)
            if coef < 0:
                equation += "-" + str(abs(coef)) + "x^" + str(d)
        else:
            if coef > 0:
                equation += " + " + str(coef) + "x^" + str(d)
            if coef < 0:
                equation += " - " + str(abs(coef)) + "x^" + str(d)
    return equation + " = 0"

# eq1 = createEquation()
# print((eq1.replace('x^1','x').replace('x^0, '')).replace('1x^','x'))
# eq2 = createEquation()
# print((eq2.replace('x^1','x').replace('x^0, '')).replace('1x^','x'))


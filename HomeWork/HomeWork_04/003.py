# 5 . Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from pathlib import Path


def file_readline_to_str(path: Path) -> str:
    with open(path, 'r') as file:
        return file.readline()


def get_coefficients_of_polynomial(poly: list) -> list:
    coefficients = []
    for i in poly:
        if ('x' in i) and ('(' in i):
            coefficients.append(
                [int(i[i.find('(')+1:i.find(')')]), int(i[0:i.find('*')])])
        elif ('x' in i) and ('(' not in i):
            coefficients.append([1, int(i[0:i.find('*')])])
        elif ('x' not in i) and (i != '+') and (i != '=') and (i != '0'):
            coefficients.append([0, int(i)])
    return coefficients


path1 = Path('les4_1.txt')
path2 = Path('les4_2.txt')
poly1 = file_readline_to_str(path1)
poly2 = file_readline_to_str(path2)
split_poly1 = poly1.split()
split_poly2 = poly2.split()
coef_list1 = get_coefficients_of_polynomial(split_poly1)
coef_list2 = get_coefficients_of_polynomial(split_poly2)

sum_str = str()

for i in coef_list1:

    for j in coef_list2:
        if (j[0] == i[0] > 1):
            sum_str += f'{i[1]+j[1]}*x**({i[0]}) + '
        elif (j[0] == i[0] == 1):
            sum_str += f'{i[1]+j[1]}*x + '
        elif (j[0] == i[0] == 0):
            sum_str += f'{i[1]+j[1]} + '

sum_str = sum_str[0:len(sum_str)-2]+'= 0'

path = Path("les5sum.txt")
with open(path, 'w') as poly:
    poly.writelines(f'{sum_str}\n')
print(f'\nФайл записан в {path}\n')
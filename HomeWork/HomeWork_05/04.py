# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc


def rle_code(data):
    encoding = ""
    prev_char = ""
    count = 0
    if not data:
        return ""
    for char in data:
        if char != prev_char:
            encoding += prev_char + str(count)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += prev_char + str(count)
    pos = 0
    encoding = encoding[0:pos] + encoding[pos + 1 :]
    return encoding
    print()

var_1 = "aaaaaaabbbbbbccccccccc"
with open("Rle01.txt", "w") as data:
    data.write(var_1)
with open("Rle01.txt", "r") as f:
    enter = f.read()

new_val_rle = rle_code(enter)
print(new_val_rle)

with open("Rle02.txt", "w") as data:
    data.write(new_val_rle)

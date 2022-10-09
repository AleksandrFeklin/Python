from HW import createEquation


def readEquation():
    firstEquation = createEquation()
    eqation = {}
    # eqation[key] = w453 -словарь ключ

    firstEquation = firstEquation.replace(" + ", " +").replace(" - ", " -").split()[:-2]
    for i in range(len(firstEquation)):
        firstEquation[i] = firstEquation[i].replace("+", "").split("x^")
        eqation[int(firstEquation[i][1])] = int(firstEquation[i][0])
    return eqation

finalWord = {}
word1 = readEquation()
word2 = readEquation()
print(word1)
print(word2)


for i in range(max(len(word1), len(word2)),-1,-1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0)
print(finalWord)

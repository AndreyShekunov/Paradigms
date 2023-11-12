# Условие
# На вход подается: список целых чисел arr

# Задача 2
# Реализовать императивную функцию, которая возвращает три числа:
# Долю позитивных чисел
# Долю нулей
# Долю отрицательных чисел

def imperative(arr):
    positive = 0
    negative = 0
    zero = 0
    for elem in arr:
        if elem > 0:
            positive += 1
        elif elem < 0:
            negative += 1
        else:
            zero += 1
    positive = positive / len(arr)
    negative = negative / len(arr)
    zero = zero / len(arr)
    return positive, negative, zero

print(imperative([1, 4, 0, -8, -5, 0, 1, 2, -4, 0]))
# (0.4, 0.3, 0.3)

# Реализовать декларативную функцию, которая возвращает три числа:
# Долю позитивных чисел
# Долю нулей
# Долю отрицательных чисел

def declarative(arr):
    positive = len(list(filter(lambda x: x > 0, arr)))
    negative = len(list(filter(lambda x: x < 0, arr)))
    zero = len(list(filter(lambda x: x == 0, arr)))
    list_num = [positive,negative,zero]

    return list(map(lambda x: x / len(arr), list_num))

print(declarative([1, 4, 0, -8, -5, 0, 1, 2, -4, 0]))
# (0.4, 0.3, 0.3)
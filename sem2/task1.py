# Задача 1. След матрицы (структурная)

# Контекст
# След матрицы - это сумма чисел на её главной диагонали. 
# След определен только для квадратных матриц (количество столбцов = количеству строк)
#
# Задача
# Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxM.
#
# Решение:
array = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
summ = 0
for i in range(len(array)):
    summ += array[i][i]
print(f"Структурная реализация: {summ}")

# Реализовать процедурную и структурную реализацию вычисления следа для любой матрицы NxM.
# 
# Решение:
def sum_arr(array):
    summ = 0
    for i in range(len(array)):
        summ += array[i][i]
    return summ

print(f"Процедурная и структурная реализация: {sum_arr(array)}")
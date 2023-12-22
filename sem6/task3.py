# Задача 3: Сортировка слиянием

# Контекст

# Ещё один известный и довольно эффективный алгоритм
# сортировки массива - сортировка слиянием (merge sort).
# Алгоритм делится на два этапа:
#     - этап разбиения - массив разбивается на пару
#       массивов до тех пор пока, полученные массивы не
#       станут массивами длины 1 (состоящими из одного
#       элемента).
#     - этап слияния - соединяем пары массивов в большие
#       массивы так, чтобы полученные массивы были
#       отсортированы.

# Ваша задача

# Реализовать сортировку слиянием на любом языке в любой парадигме.
# На вход ваша программа получает массив из чисел, а вернуть должна отсортированный
# массив.
def input_list(lst):
    if len(lst) > 1:
        left = lst[:len(lst) // 2]
        right = lst[len(lst) // 2:]
        left = input_list(left)
        right = input_list(right)
        return concat(left, right)
    return lst


def concat(lst_one, lst_two):
    result_list = []
    i = 0
    j = 0

    while i < len(lst_one) and j < len(lst_two):
        if lst_one[i] < lst_two[j]:
            result_list.append(lst_one[i])
            i += 1
        else:
            result_list.append(lst_two[j])
            j += 1

    while i < len(lst_one):
        result_list.append(lst_one[i])
        i += 1

    while j < len(lst_two):
        result_list.append(lst_two[j])
        j += 1

    return result_list


lst = [4, 6, 8, 7, 2, 1, 9, 10, 11, 3]

print(input_list(lst))

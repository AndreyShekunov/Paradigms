# Задача №1
# Дан список целых чисел numbers. 
# Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки
def bubble_sort_descending(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                
numbers = [1, 5, 3, 8, 7, 2, 4, 6, 9]
bubble_sort_descending(numbers)
print('Сортировка по убыванию:', numbers)

# Написать точно такую же процедуру, но в декларативном стиле
def sort_descending(nums):
    return sorted(nums, reverse=True)

nums = [64, 34, 25, 12, 22, 11, 90]
sorted_descending_numbers = sort_descending(numbers)
print("Сортировка по убыванию:", sorted_descending_numbers)
# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа 
# target узнать содержится ли target в array. Такую процедуру будем называть поиском.

# Задача 1
# Реализовать императивную функцию поиска элементов на языке Python.

def search_imperative(number, list):
    for i in range(len(list)):
        if list[i] == number:
            return True
    return False


print(search_imperative(5, [2, 3, 4, 9]))

# Реализовать декларативную функцию поиска элементов на языке Python.

def search_declarative(number, list):
    return number in list


print(search_declarative(5, [2, 5, 4, 9]))
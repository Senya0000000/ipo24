import numpy as np


def add_element_to_array(arr):
    # Вычисляем сумму элементов с положительными значениями
    positive_sum = np.sum(arr[arr > 0])

    # Вычисляем сумму элементов с отрицательными значениями
    negative_sum = np.sum(arr[arr < 0])

    # Вычисляем модуль отрицательной суммы
    negative_sum_abs = abs(negative_sum)

    # Вычисляем значение нового элемента
    new_element = negative_sum_abs - positive_sum

    # Добавляем новый элемент в конец массива
    arr = np.append(arr, new_element)

    return arr
N = 5
my_array = np.array([-2, 4, -1, 3, -5])
result_array = add_element_to_array(my_array)
print(result_array)
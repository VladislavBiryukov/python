"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

array = [random.randint(-100, 100) for _ in range(5)]
print(f"начальный массив - {array}")
_min = 0
_max = 0
for i in range(len(array)):
    if array[i] < array[_min]:
        _min = i
    elif array[i] > array[_max]:
        _max = i

array[_min], array[_max] = array[_max], array[_min]
print(f"массив с заменой минимального и максимального элемента - {array}")

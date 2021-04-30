"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

matrix = [[random.randint(0, 100) for _ in range(8)] for _ in range(8)]

for line in matrix:
    print(*line, sep='\t')


max_ = None

for j in range(len(matrix[0])):
    min_ = matrix[0][j]

    for i in range(len(matrix)):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]

    if max_ is None or max_ < min_:
        max_ = min_

print(f'максимальный среди минимальных = {max_}')

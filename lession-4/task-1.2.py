"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
***
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


import random
import timeit
import cProfile
def max_min(matrix):


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
    return(f'максимальный среди минимальных = {max_}')

size = 1
while size != 100:
    size *= 10
    matrix = [[random.randint(size * -10,size * 10) for _ in range(size)] for _ in range(size)]
    print(timeit.timeit('max_min(matrix)', number=1000, globals=globals()))
# 10 - 0.39743122099999995
# 20 -  так и не дождался конца работы программы
# 50 -  так и не дождался конца работы программы
# 100 - 38.573714761
#cProfile.run('max_min(matrix)')

#205 function calls in 0.040 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.040    0.040 <string>:1(<module>)
#        1    0.001    0.001    0.040    0.040 task-1.2.py:11(max_min)
#        1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
#      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      100    0.039    0.000    0.039    0.000 {built-in method builtins.print}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Process finished with exit code 0



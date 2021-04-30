"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
***
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random
import timeit
import cProfile
def max_min(size):

    matrix = [[random.randint(size * -10,size * 10) for _ in range(size)] for _ in range(size)]

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

print(timeit.timeit('max_min(10)', number=1000, globals=globals())) # 0.525775757
print(timeit.timeit('max_min(20)', number=1000, globals=globals())) # 2.03300342
print(timeit.timeit('max_min(50)', number=1000, globals=globals())) # 12.964601706
print(timeit.timeit('max_min(100)', number=1000, globals=globals())) # 51.134139352000005


cProfile.run('max_min(100)')

#50432 function calls in 0.061 seconds

#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.066    0.066 <string>:1(<module>)
#    10000    0.007    0.000    0.015    0.000 random.py:200(randrange)
#    10000    0.004    0.000    0.019    0.000 random.py:244(randint)
#    10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#       1    0.001    0.001    0.065    0.065 task-1.py:10(max_min)
#       1    0.000    0.000    0.023    0.023 task-1.py:12(<listcomp>)
#        1    0.000    0.000    0.066    0.066 {built-in method builtins.exec}
#      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      100    0.041    0.000    0.041    0.000 {built-in method builtins.print}
#    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    10226    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

#Process finished with exit code 0

"""
На сколько я понял 50432 раза обратились к функции, за очень короткое время, против 205 через циклы, почти за то же время, 
но с параметрами 20 и 50 я не дождался результата.
к сожалению 3ий вариант я не придумал...
"""
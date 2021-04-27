"""
Определить, какое число в массиве встречается чаще всего.
"""

from random import random

N = 20
array = [0] * N
for i in range(N):
    array[i] = int(random() * 20)
print(array)

num = array[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(f"число {num}, встречается -  {max_frq} раз")
else:
    print('Все элементы уникальны')

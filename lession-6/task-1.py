"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
import sys

# решение через переменные с уловием.
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if b < a < c or c < a < b:
    print(f"Среднее число является {a}")
elif a < b < c or c < b < a:
    print(f"Среднее число является {b}")
else:
    print(f"Среднее число является {c}")


print(f'первая переменная хранит - {sys.getrefcount(a)} байт')
print(f'вторая переменная хранит - {sys.getrefcount(b)} байт')
print(f'третья переменная хранит - {sys.getrefcount(c)} байт')
sum_mem = (sys.getrefcount(a) + sys.getrefcount(b) + sys.getrefcount(c))
print(f'сумма 3х переменных = {sum_mem} байт' )

print('*' * 100)

# решение через цикл с условием
a1, b2, c3 = [x for x in input('Введите три числа, через пробел: ').split()]

if b2 < a1 < c3 or c3 < a1 < b2:
    print(f'Среднее: {a}')
elif a1 < b2 < c3 or c3 < b2 < a1:
    print(f'Среднее: {b2}')
else:
    print(f'Среднее: {c3}')

print(f'первая переменная хранит - {sys.getrefcount(a1)} байт')
print(f'вторая переменная хранит - {sys.getrefcount(b2)} байт')
print(f'третья переменная хранит - {sys.getrefcount(c3)} байт')
sum_mem_1 = (sys.getrefcount(a1) + sys.getrefcount(b2) + sys.getrefcount(c3))
print(f'сумма 3х переменных = {sum_mem_1} байт' )

print('*' * 100)

#Вывод: В моем случае при одинаковых значениях переменных, через цикл информация занимает меньше места.


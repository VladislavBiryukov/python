"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""
numb = input("Введите целое 3х значное число: ")
amount = 0
composition = 1
for numbs in numb:
    amount = amount + int(numbs)
    composition = composition * int(numbs)
print(f"Сумма цифр {numb} = {amount}")
print(f"Произведение цифр {numb} = {composition}")
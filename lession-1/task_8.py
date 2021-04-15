"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
name = str(input("Как вас зовут? "))
year = int(input(f"{name.title()}, введите год: "))
if (year % 4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f"{name.title()}! {year} - является високосным!")
else:
    print(f"{name.title()}! {year} - является не високосным!")
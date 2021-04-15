"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
name = str(input("Как вас зовут? "))
alf_numb  = int(input(f"{name.title()}, введите номер буквы в алфавите: "))

alf_list = [chr(n) for n in range(ord('A'), ord('Z') + 1)]
if alf_numb <= len(alf_list):
    print(f'{name.title()}, буква под номером {alf_numb }: является - {alf_list[alf_numb - 1]}')
else:
    print(f'{name.title()}, введеное число не входит в диапазон букв в алфавите ({len(alf_list)})')


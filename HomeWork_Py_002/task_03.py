# ЗАДАЧА: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


number = int(input('Введите число: '))
i = 1
while i < number:
    print(i)
    i *= 2

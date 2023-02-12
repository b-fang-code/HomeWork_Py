# ЗАДАЧА:Напишите программу, которая на вход принимает два числа A и B, и возводит число А# в целую степень B
# с помощью рекурсии.

number_a = int(input('Введите число А: '))
number_b = int(input('Введите число В: '))


def recur(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return (a * (recur(a, b - 1)))


print(f'Число {number_a} в степени {number_b} равно {recur(number_a, number_b)}')

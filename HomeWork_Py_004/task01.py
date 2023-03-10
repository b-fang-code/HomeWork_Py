# ЗАДАЧА: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


# quantity_1 = int(input('Введите количество элементов первого множества: '))
# quantity_2 = int(input('Введите количество элементов второго множества: '))
#
# list_1 = []
# list_2 = []
#
# for i in range(quantity_1):
#     list_1.append(int(input(f'Введите {i + 1} элемент первого множества: ')))
# print('Достаточно! ')
#
# for i in range(quantity_2):
#     list_2.append(int(input(f'Введите {i + 1} элемент второго  множества: ')))
# print('Достаточно! ')
#
#
# print(f'Первое множество: {list_1}')
# print(f'Второе множество: {list_2}')
# list_1 = set(list_1)
# list_2 = set(list_2)
#
# list_3 = list_1.intersection(list_2)
# list_3 = list(list_3)
# list_3.sort()
# print(f'Повторяющиеся числа: {list_3}')

# -------------------------------------------------------------------------------------------------------------
#  2й СПОСОБ:

import random

first_size = int(input('Введите размер первого списка: '))
second_size = int(input('Введите размер второго списка: '))

first_list = [random.randint(0, 20) for _ in range(first_size)]
second_list = [random.randint(0, 20) for _ in range(second_size)]

print(first_list)
print(second_list)

final_list = []
for item in first_list:
    if item in second_list:
        final_list.append(item)

final_list.sort()
print(final_list)


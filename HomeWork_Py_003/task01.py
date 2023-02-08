# ЗАДАЧА: Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

length_list = int(input('Введите длинну списка: '))
number = int(input('Введите искомое число: '))

my_list = []

for i in range(length_list):
    my_list.append(random.randint(1, 100))
print(f'Исходный список: {my_list}')

count_number = 0
for i in range(length_list):
    if my_list[i] == number:
        count_number += 1
print(f'В данном списке искомое число встречается {count_number} раз')

new_list = my_list.copy()
new_list.append(number)
new_list = set(new_list)
new_list = list(new_list)
new_list.sort()
print(f'new {new_list}')
print(f'my {my_list}')

near_num_min = 0
near_num_max = 0
for i in range(len(new_list)):
    if new_list[i] == number and number != new_list[0]:
        near_num_max = new_list[i + 1]
        near_num_min = new_list[i - 1]
    else:
        if new_list[i] == number:
            near_num_max = new_list[i + 1]
print(f'Максимально близкое по значению число это {near_num_min} и {near_num_max}')

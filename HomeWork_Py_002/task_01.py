# ЗАДАЧА: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
# # одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2

from random import randint

count_tail = 0           # количество решек
count_eagle = 0          # количество орлов
count_coins = int(input('Введите количество монет:'))
for _ in range(count_coins):
    side_coin = randint(0, 1)
    print(side_coin)
    if side_coin == 0:
        count_eagle += 1
    else:
        count_tail += 1
print(f'орлов {count_tail}')
print(f'решек {count_eagle}')
if count_eagle < count_tail:
    print(f'Нужно перевернуть {count_eagle} монет')
else:
    print(f'Нужно перевернуть {count_tail} монет')

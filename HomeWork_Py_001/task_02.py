# ЗАДАЧА: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

sum = int(input('Сколько всего сделано журавликов? : '))
if sum % 3 != 0:
    print('С данным числом условия не соблюдаются!')
else:
    kate = int(sum // 3) * 2
    boys = int(kate // 2) // 2
    print(f'Катя сделала {kate} журавликов, а Петя и Серёжа по {boys} журавликов')

# ЗАДАЧА: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из
# одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке.
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод: Парам пам-пам

poem = (input('Введите кричалку: '))
poem_1 = poem.split()
vowel_list = set('аеиоёуэюя')
result = list()
for item in poem_1:
    count = 0
    for letter in item:
        if letter in vowel_list:
            count += 1
    result.append(count)

if len(set(result)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')

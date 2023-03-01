def menu() -> int:
    print('''Главное меню
    1. Открыть контакт
    2. Сохранить контакт
    3. Показать контакт
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    while True:
        choice = (input('Выберите пункт меню: '))
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def show_contact(phone_book: list):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print()
    else:
        print('\nТелефонная книга не открыта или пуста\n')


def new_contact() -> dict:
    print()
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def change_contact(book: list) -> tuple:
    show_contact(book)
    choice = int(input('Введите контакт, который хотите изменить: '))
    name = input('Введите новое имя или Enter оставить без изменений: ')
    phone = input('Введите новый телефон или Enter оставить без изменений: ')
    comment = input('Введите новый комментарий или Enter оставить без изменений: ')
    return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                        'phone': phone if phone else book[choice - 1].get('phone'),
                        'comment': comment if comment else book[choice - 1].get('comment')}


def select_to_delete(book: list):
    show_contact(book)
    return int(input('Введите номер элемента, который хотите удалить: ')) - 1


def input_request(text: str) -> str:
    return input(f'Введите {text}: ')

def goodbye():
    print('Всего хорошего!')

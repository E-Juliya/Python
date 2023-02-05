

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']

def main_menu():
    print('Главное меню: ')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}.{item}')
    choice = int(input('Выберите пункт меню: '))
    return choice


phone_book = []

path = 'phone_book.txt'


def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    print(file)


phone_book = []
path = 'HomeWork\HW_phone\phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book
    

def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))
    print(phone_book)

def save_file():
    global phone_book
    global path
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact)) 
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(pb_str))
    message = 'Файл сохранён'
    return message
    
def delete_contact(id_contact: int):
    global phone_book
    phone_book.pop(id_contact - 1)
    message = 'Контакт удалён'
    return message

def update_contact(changed_contact: list, id_contact: int):
    global phone_book
    for i, item in enumerate(changed_contact):
        if item:
            phone_book[id_contact - 1][i] - item

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)

def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result
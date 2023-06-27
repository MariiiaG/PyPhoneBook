# Все функции с print и input остаются в console. 
from .text import *

def menu() -> int: #ничего не принимает, на выходе инт
    print(main_menu)
    while True :
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 9 : # так как в нашем меню только 8 позиций
            return int(choice)
        print(input_error)
        
        
def print_message(message: str) :
    length = len(message)
    print('\n' + '=' * length)
    print(message)
    print('=' * length + '\n')

        
def show_contacts(book: list[dict[str, str]]): # a list of dicts with str key and str value 
    if book: # if there's anything inside the book
        print('\n' + '=' * 67) # 67 is approximate length of the message here
        for contact in book :
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment') 
            print(f'{uid:>3}. {name:<20} {phone:<20} {comment:<20}') 
        print('=' * 67 + '\n')
    else :
        print(book_error)
         

def input_contact(message: str) -> dict[str, str] :
    print(message)
    name = input(new_contact[0])
    phone = input(new_contact[1])
    comment = input(new_contact[2])
    return {'name': name, 'phone': phone, 'comment': comment}

def input_return(message: str) -> str :
    return input(message)
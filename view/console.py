from .text import main_menu, menu_choice, input_error

def menu() -> int: #ничего не принимает, на выходе инт
    print(main_menu)
    choice = input(menu_choice)
    if choice.isdigit() and 0 < int(choice) < 9 : # так как в нашем меню только 8 позиций
        return int(choice)
    print(input_error)
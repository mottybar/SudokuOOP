from SudokuBoard import Board
from MenuFactory import MenuFactory

def add_menu_option(text):
    return "\n\t"+text

def get_user_choice_from_menu():
    text = "Enter choice:"
    text += add_menu_option("i - set suduko size")
    text += add_menu_option("a - add/override number")
    text += add_menu_option("r - remove number")
    text += add_menu_option("s - solve Suduko (initial size is 3)")
    text += add_menu_option("c - show current board")
    text += add_menu_option("n - add random numbers")
    text += add_menu_option("m - clear board")
    text += add_menu_option("q - quit")
    print(text)
    
    return input(">")


def main():
    menu_factory = MenuFactory()
    board = Board()
    board.set_size(3)
    board.show()
    while (True):
        choice = get_user_choice_from_menu()
        next_method = menu_factory.get_menu_method(choice)
        # Run the next method
        next_method()


main()
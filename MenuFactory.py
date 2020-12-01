from menu_options import *
"""
Menu factory class gives us a factory for the menu, we send the user choice and get the next method to run
"""
class MenuFactory:
    def __init__(self):
        self.menu_dictionary = {
            "i": set_board_size,
            "a": add_or_override_number,
            "r": remove_number,
            "s": find_solution,
            "c": show_current_board,
            "n": add_random_numbers,
            "m": clear_board,
            "q": exit_program
        }

    def get_menu_method(self, menu_option):
        return self.menu_dictionary.get(menu_option, print_option_not_exists)

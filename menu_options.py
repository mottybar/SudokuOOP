from validations import *
from SudokuBoard import Board


def not_implemented():
   print("This option was not implemented yet")

"""
Menu option i -> set board size
"""
def set_board_size():
    size = input("Enter size of sudoku: ")
    if not size.isdigit():
        print("The size you entered is not a valid number")
        return
    size = int(size)
    if size > 10:
        print("size too big, the limit is 10")
        return
    board = Board()
    board.set_size(size)

"""
Menu option a -> add/override number
"""
def add_or_override_number():
    row = input("Row number:")
    if not is_valid_size_num(row):
        print("Wrong size")
        return

    column = input("Column number:")
    if not is_valid_size_num(column):
        print("Wrong size")
        return

    value = input("value:")
    if not is_valid_size_num(value):
        print("Wrong size")
        return

    restore = Board().board[int(row)-1][int(column)-1]

    Board().board[int(row) - 1][int(column) - 1] = [False]*(Board().get_size())**2

    if  is_valid_sudoku_board(int(row)-1,int(column)-1,int(value)-1):
        Board().board[int(row) - 1][int(column) - 1][int(value) - 1] = True
        print("The value you entered is valid sudoku-wise")

    else:
        print("The value you entered is not valid sudoku-wise")
        Board().board[int(row)-1][int(column)-1] = restore

"""
Menu option r -> remove number
"""
def remove_number():
    row = input("Row number:")
    if not is_valid_size_num(row):
        print("Wrong size")
        return

    column = input("Column number:")
    if not is_valid_size_num(column):
        print("Wrong size")
        return
    size = Board().get_size()
    Board().board[int(row) - 1][int(column) - 1] = [False]*size**2   # TODO: Move to a method inside the Board class


"""
Menu option c -> exit the program
"""
def show_current_board():
   board = Board()
   board.show()


"""
Menu option n -> add random numbers
"""
def add_random_numbers():
    num_of_random_numbers = input("Enter number of random numbers: ")
    if not is_valid_num_of_random_numbers(num_of_random_numbers):
        print("Wrong size")
        return
    board = Board()
    I = board.get_size() ** 2
    max_try = 10
    num_try = 0
    num_to_add = int(num_of_random_numbers)
    while (num_to_add > 0 and num_try < max_try):
        random_num = np.random.randint(0,I)
        empty_cells = board.get_empty_cells()
        random_cell_index = np.random.randint(len(empty_cells))
        i,j = empty_cells[random_cell_index]
        if is_valid_sudoku_board(i, j, random_num):
            board.board[i][j][random_num] = True
            num_to_add -= 1
            num_try = 0
        else:
            num_try += 1
        board.show()
        x=0




"""
Menu option m -> clear board
"""
def clear_board():
    board = Board()
    board.clear()


"""
Menu option q -> exit the program
"""
def exit_program():
   print("Goodbye.")
   exit(0)

"""
Default menu option for non existing keys 
"""
def print_option_not_exists():
   print("wrong choice")

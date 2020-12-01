from mip import *
from SudokuBoard import Board
import numpy as np


def is_valid_size_num(num):
    #Do not accept non numeric ("five" is not ok, 5.5 is  not ok, -5 is not ok)
    if not num.isdigit():
        return False
    num = int(num)
    #DO not accept higer then 9 (3x3)
    if num > Board().get_size()**2:
        return False
    #Do not accept 0
    if num <= 0:
        return False

    return True  # Only if all the validations are ok

def is_valid_num_of_random_numbers(num_of_random_numbers):
    if not num_of_random_numbers.isdigit():
        return False
    num_of_random_numbers = int(num_of_random_numbers)
    empty_cells = Board().get_empty_cells()
    if  num_of_random_numbers > len(empty_cells):
        print("number of random numbers can't be bigger than empty cells")
        return False
    return True  # Only if all the validations are ok






def is_valid_sudoku_board(row, col, value):
    valid = True
    board = Board()
    for c in range(board.get_size() ** 2):
        if board.board[row][c][value] == True:
            print("row valid error")
            valid = False
    for r in range(board.get_size() ** 2):
        if board.board[r][col][value] == True:
            print("column valid error")
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range (board.get_size()):
        for y in range (board.get_size()):
            if board.board[rowsection * 3 + x][colsection * 3 + y][value] == True:
                print ("cube valid error")
                valid = False
    return valid














def find_solution():
    board = Board()
    size_of_cube = board.get_size()
    size_of_board = board.get_size()**2
    I = range(board.get_size()**2)
    m = Model('model.lp')

    #x = [m.add_var(var_type=BINARY) for i in I]
    A = m.add_var_tensor(shape=(size_of_board, size_of_board, size_of_board), name="tensor", var_type=BINARY)
    #generic constraints
    for r in I:          #constraint each number appears one time in each row
        for number in I:
             m += xsum(A[r,:,number]) == 1
    for c in I:      #constraint each number appears one time in each column
        for number in I:
            m += xsum(A[:, c, number]) == 1
    for i in range(size_of_cube):     #constraint each number appears one time in each cube
        for j in range(size_of_cube):
            for number in I:
                m+=A[i*size_of_cube:(i+1)*size_of_cube,j*size_of_cube:(j+1)*size_of_cube,number].sum() == 1
    for r in I:    #constarint exactly one number each cell
        for c in I:
            m += xsum(A[r, c, :]) == 1
    # specific constraints
    for r in I:
        for c in I:
            for v in I:
                if board.board[r][c][v]:
                    m += A[r, c, v] == 1
    # m += A[4,5,7] == 1 #constarint for A[4,5] = 8
    # m += A[4,6,7] == 1 #constarint for A[4,6] = 8


    m.optimize()
    solution = convert_binary_to_sudoku(A)
    solution.show()


    if not m.num_solutions:
        print("no solutions")
        return False
    print("a solution was found")
    return True

def convert_binary_to_sudoku(A):
    board = Board()
    I = range(board.get_size() ** 2)
    for r in I:
        for c in I:
            for v in I:
                board.board[r][c][v] = A[r][c][v].xi(0)
    return board

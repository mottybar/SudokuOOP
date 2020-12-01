"""
Board is a singleton implements class which represents a single board
"""
class Board:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

    @staticmethod
    def convert_column_list_to_numeric_value(column):
        for index, value in enumerate(column):
            if value:
                return " "+str(index + 1)+" "
        return " - "

    def show(self):
        col_index=''
        for i in range(len(self.board[1])):
            col_index += str(i) + "  "
            if (i + 1) %self.board_size == 0:
                col_index += "   "
        print("   " + col_index)
        for row_index, row in enumerate(self.board):
            text = ""
            for column_index, column in enumerate(row):
                text += self.convert_column_list_to_numeric_value(column)
                if (column_index+1) % self.board_size == 0:
                    text += " | "
            print(str(row_index)+ " " + text)
            if (row_index+1) % self.board_size == 0:
                print("-"*40)

    def set_size(self, size):
        # [False * 9] // Cell
        # [[False * 9] for k in range(size)] // row
        # [[[False * 9] for k in range(size)] for j in range(size)] // Table
        self.board_size = size
        self.board = [[[False]*(size*size) for k in range(size*size)] for j in range(size*size)]

        #Temp - adding values
        self.board[0][0][0] = True
        self.board[2][5][7] = True
        self.board[1][8][3] = True


    def get_size(self):
        return self.board_size

    def clear(self):
        for i in range(self.board_size**2):
            for j in range(self.board_size**2):
                for k in range(self.board_size**2):
                    self.board[i][j][k] = False

    def get_empty_cells(self):
        empty_cells=[]
        for i in range(self.board_size**2):
            for j in range(self.board_size**2):
                if not any (self.board[i][j]):    #return False if the cell is empty (all binary numbers are false)
                    empty_cells.append((i,j))
        return empty_cells



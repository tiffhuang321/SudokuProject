import random


# initiate sudoku board with generate_sudoku() at end of file
class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.removed_cells = removed_cells
        self.row_length = row_length
        self.board = [["-" for x in range(9)] for y in range(9)]
        self.box_length = 3

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        self.row = row
        self.num = num
        return False if self.num in self.board[self.row] else True

    def valid_in_col(self, col, num):
        self.col = col
        self.num = num
        for row in self.board:
            if row[col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        self.row_start = row_start
        self.col_start = col_start
        self.num = num

        box = [self.board[self.row_start][self.col_start:self.col_start + 3]
               + self.board[self.row_start + 1][self.col_start:self.col_start + 3]
               + self.board[self.row_start + 2][self.col_start:self.col_start + 3]]
        for value in box:
            for number in value:
                if number == self.num:
                    return False
        return True

    def is_valid(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num

        if not self.valid_in_row(self.row, self.num):
            return False
        if not self.valid_in_col(self.col, self.num):
            return False
        if self.row % 3 != 0 or self.col % 3 != 0:
            self.row = self.row - self.row % 3
            self.col = self.col - self.col % 3
            if not self.valid_in_box(self.row, self.col, self.num):
                return False
        return True

    def fill_box(self, row_start, col_start):
        self.row_start = row_start
        self.col_start = col_start

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        box = []

        box.append(self.board[self.row_start][self.col_start:self.col_start + 3])
        box.append(self.board[self.row_start + 1][self.col_start:self.col_start + 3])
        box.append(self.board[self.row_start + 2][self.col_start:self.col_start + 3])

        for i, row in enumerate(box):
            for j, item in enumerate(row):
                random_number = random.choice(numbers)
                box[i][j] = random_number
                numbers.remove(random_number)

        for i, row in enumerate(box):
            for j, item in enumerate(row):
                self.board[self.row_start+i][self.col_start+j] = box[i][j]

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        zero = 0
        while True:
            if zero == self.removed_cells:
                break
            random_index = random.randrange(9)
            random_row = self.board[random_index]
            random_col = random_row.index(random.choice(random_row))
            if self.board[random_index][random_col] != 0:
                self.board[random_index][random_col] = 0
                zero += 1


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

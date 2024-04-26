import pygame, sys
import SudokuGenerator

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
CELL_SIZE = 70


class Cell:
    def __init__(self, value, row, col, screen):  # value = SudokuGenerator
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = None

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    # added for to make life easier
    def get_cell_value(self):
        return self.value

    def draw(self):
        number_font = pygame.font.Font(None, 40)
        rectangle = pygame.Rect((self.col * 70, self.row * 70), (70, 70))
        valid_cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # render values not equal to zero
        if self.value in valid_cell:
            number = number_font.render(str(self.value), 0, (0, 0, 0))
            number_place = number.get_rect(center=(self.col * 70 + 35, self.row * 70 + 35))
            self.screen.blit(number, number_place)

        # draws the sketched values
        if self.sketched_value:
            if self.value == 0:
                number = number_font.render(str(self.sketched_value), 0, (140, 140, 140))
                number_place = number.get_rect(center=(self.col * 70 + 15, self.row * 70 + 15))
                self.screen.blit(number, number_place)
            else:
                self.sketched_value = None

        # draws the rectangle when cell is selected
        if self.selected is True:
            pygame.draw.rect(self.screen, (255, 0, 0), rectangle, 2)


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = [rows[:] for rows in SudokuGenerator.generate_sudoku(9, self.difficulty)]
        self.unsolved_board = [rows[:] for rows in self.board[1]]
        self.cells = []
        '''
        self.board[0] = solution board
        self.board[1] = player board
        self.unsolved_board = copy of an unedited player board containing all empty (zero) values
        self.cells = copy of each value on the player board returned as a 2d list of Cells
        '''
        self.selected_cell = None

    def draw(self):
        self.screen.fill((255, 255, 245))
        # draw horizontal lines
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(self.screen, BLACK, (0, i * CELL_SIZE), (630, i * CELL_SIZE), 2)
            else:
                pygame.draw.line(self.screen, BLACK, (0, i * CELL_SIZE), (630, i * CELL_SIZE))

        # draw vertical lines
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(self.screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, 630), 2)
            else:
                pygame.draw.line(self.screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, 630))

        # insert values into the Cell class and project each drawn value onto the board
        for x, values in enumerate(self.board[1]):
            for y, number in enumerate(values):
                cell = Cell(number, x, y, self.screen)
                cell.draw()
                self.cells.append(cell)

        if len(self.cells) == 81:
            self.cells = [self.cells[i:i + 9] for i in range(0, len(self.cells), 9)]

    def select(self, row, col):
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True
        self.selected_cell.draw()

    def click(self, x, y):

        # return None if the board is not drawn
        if len(self.cells) == 0:
            return None

        row = y // 70
        col = x // 70

        self.select(row, col)
        return row, col

    def clear(self):
        for i, row in enumerate(self.unsolved_board):
            for j, cell in enumerate(row):
                if self.cells[i][j].get_cell_value() != self.unsolved_board[i][j]:
                    self.selected_cell.set_cell_value(0)
        self.selected_cell.set_sketched_value(None)
        self.update_board()

    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        self.draw()
        self.selected_cell.draw()

    # cannot place number when there is no initial sketched value
    def place_number(self, value):
        if self.selected_cell.sketched_value:
            self.selected_cell.set_cell_value(value)
            self.update_board()

    def reset_to_original(self):
        for i, row in enumerate(self.board[1]):
            for j, cell in enumerate(row):
                self.board[1][i][j] = self.unsolved_board[i][j]
                self.cells[i][j] = Cell(self.unsolved_board[i][j], i, j, self.screen)

    # returns True if there are no more empty cells, else False
    def is_full(self):
        if self.find_empty is None:
            return True
        return False

    # updates self.board[1], which is where the main board values are taken and drawn
    def update_board(self):
        for i, row in enumerate(self.board[1]):
            for j, cell in enumerate(row):
                if self.cells[i][j].get_cell_value() != Cell(cell, i, j, self.screen).get_cell_value():
                    self.board[1][i][j] = self.cells[i][j].get_cell_value()

    def find_empty(self):
        for x, row in enumerate(self.board[1]):
            for y, col in enumerate(row):
                if self.board[1][x][y] == 0:
                    return x, y

    # returns False if the player board does not match up with the solution board, else True
    def check_board(self):
        for i, row in enumerate(self.board[1]):
            for j, cell in enumerate(row):
                if self.board[0][i][j] != self.board[1][i][j]:
                    return False
        return True

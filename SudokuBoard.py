import pygame
import sys
pygame.init()
from SudokuGenerator import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.sketched_value = 0
        self.selected = False # to indicate if cell is selected

        self.font = pygame.font.Font(None, 36) # font
        self.cell_size = 50 # cell size

        self.xcord = (self.col) * self.cell_size
        self.ycord = (self.row) * self.cell_size

        self.cell_border_color = "black"
        self.cell = pygame.Rect(self.xcord, self.ycord, self.cell_size, self.cell_size)

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row

    def set_cell_value(self, value):
        self.value = value

    def get_sketched_value(self):
        return self.sketched_value

    def set_sketched_value(self, value):
        # stuff for sketching the value inside
        self.sketched_value = value

    def draw(self):
        # reference draw_chips() function in main_gui.py
        # reference oop_main.py file

        x = self.col * self.cell_size
        y = self.row * self.cell_size
        rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

        # Draw cell outline if selected
        if self.selected:
            self.cell_border_color = "red"

        # Draw cell background
        pygame.draw.rect(self.screen, self.cell_border_color, self.cell, width = 1)

        # Draw cell value if not zero
        if self.value != 0:
            text_surface = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)


    # to handle drawing filled in cell
    def draw_sketched(self):
        pygame.draw.rect(self.screen, "black", self.cell, width=1)

        num_font = pygame.font.Font(None, 20)
        num = num_font.render(str(self.sketched_value), True, "black")
        numRect = num.get_rect(center=self.cell.center)
        self.screen.blit(num, numRect)

class Board:
    def __init__(self, width, height, screen, difficulty, correctValues, trueValues):
        self.width = width
        self.height = height
        self.square_size = width/9
        self.screen = screen
        self.difficulty = difficulty

        self.correctValues = correctValues
        self.trueValues = trueValues
        self.cells = []
        self.selected_cell = Cell(0, 0, 0, self.screen)

        self.row1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.row2 = [9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.row3 = [18, 19, 20, 21, 22, 23, 24, 25, 26]
        self.row4 = [27, 28, 29, 30, 31, 32, 33, 34, 35]
        self.row5 = [36, 37, 38, 39, 40, 41, 42, 43, 44]
        self.row6 = [45, 46, 47, 48, 49, 50, 51, 52, 53]
        self.row7 = [54, 55, 56, 57, 58, 59, 60, 61, 62]
        self.row8 = [63, 64, 65, 66, 67, 68, 69, 70, 71]
        self.row9 = [72, 73, 74, 75, 76, 77, 78, 79, 80]

        self.cells_to_check = []


    def draw(self):

        # make background white
        self.screen.fill("white")

        # set lineWidth var
        lineWidth = 0

        # draw horizontal lines
        for i in range(1, 9):
            # set the bold for the 3x3 lines
            if i == 3 or i == 6:
                lineWidth = 6
            else:
                lineWidth = 2

            # draw the line
            pygame.draw.line(self.screen, "black",
                             (0, i * self.square_size),
                             (self.width, i * self.square_size),
                             lineWidth)

        # draw vertical lines
        for i in range(1, 9):
            # set the bold for the 3x3 lines
            if i == 3 or i == 6:
                lineWidth = 6
            else:
                lineWidth = 2

            # draw the line
            pygame.draw.line(self.screen, "black",
                             (i * self.square_size, 0),
                             (i * self.square_size, self.height),
                             lineWidth)

        # create the 81 cells and put them in the cell list
        # name of cells is their index
        for row in range(0, 9):
            for col in range(0, 9):
                newCell = Cell(0, row, col, self.screen)
                newCell.set_cell_value(self.correctValues[row][col])
                self.cells.append(newCell)
                newCell.draw()




    def select(self, row, col):
        ind = 0

        if row == 1:
            ind = self.row1[col - 1]
        elif row == 2:
            ind = self.row2[col - 1]
        elif row == 3:
            ind = self.row3[col - 1]
        elif row == 4:
            ind = self.row4[col - 1]
        elif row == 5:
            ind = self.row5[col - 1]
        elif row == 6:
            ind = self.row6[col - 1]
        elif row == 7:
            ind = self.row7[col - 1]
        elif row == 8:
            ind = self.row8[col - 1]
        elif row == 9:
            ind = self.row9[col - 1]

        self.selected_cell = self.cells[ind]
        self.cells[ind].selected = True
        self.cells[ind].draw()


    def click(self, x, y):
        if x > self.width or y > self.height:
            return None
        else:
            row = 0
            col = 0

            if y < self.square_size:
                row = 1
            elif y < 2 * self.square_size:
                row = 2
            elif y < 3 * self.square_size:
                row = 3
            elif y < 4 * self.square_size:
                row = 4
            elif y < 5 * self.square_size:
                row = 5
            elif y < 6 * self.square_size:
                row = 6
            elif y < 7 * self.square_size:
                row = 7
            elif y < 8 * self.square_size:
                row = 8
            elif y < 9 * self.square_size:
                row = 9

            if x < self.square_size:
                col = 1
            elif x < 2 * self.square_size:
                col = 2
            elif x < 3 * self.square_size:
                col = 3
            elif x < 4 * self.square_size:
                col = 4
            elif x < 5 * self.square_size:
                col = 5
            elif x < 6 * self.square_size:
                col = 6
            elif x < 7 * self.square_size:
                col = 7
            elif x < 8 * self.square_size:
                col = 8
            elif x < 9 * self.square_size:
                col = 9

            return (row, col)

    def clear(self):
        self.selected_cell = ""

    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        self.selected_cell.draw_sketched()
        self.cells_to_check.append(self.selected_cell)


    def place_number(self, value):
        self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for cell in self.cells:
            cell.set_sketched_value(cell.value)

    def is_full(self):
        count = 0
        for cell in self.cells:
            if cell.get_sketched_value() != 0:
                count += 1

        answer = 0

        if self.difficulty == 30:
            answer = 30

        elif self.difficulty == 40:
            answer = 40

        elif self.difficulty == 50:
            answer = 50

        if count == answer:
            return True
        else:
            return False

    def update_board(self):
        for cell in self.cells:
            cell.set_cell_value(cell.selected_value)


    # returns rows and cols of empty cell
    def find_empty(self):
        empty = ""
        for cell in self.cells:
            if cell.sketched_value == 0:
                empty = str(self.cells.index(cell))
                break

        row = 0
        col = 0

        if empty in self.row1:
            row = 1
            col = self.row1.index(empty)
        elif empty in self.row2:
            row = 2
            col = self.row2.index(empty)
        elif empty in self.row3:
            row = 3
            col = self.row3.index(empty)
        elif empty in self.row4:
            row = 4
            col = self.row4.index(empty)
        elif empty in self.row5:
            row = 5
            col = self.row5.index(empty)
        elif empty in self.row6:
            row = 6
            col = self.row6.index(empty)
        elif empty in self.row7:
            row = 7
            col = self.row7.index(empty)
        elif empty in self.row8:
            row = 8
            col = self.row8.index(empty)
        elif empty in self.row9:
            row = 9
            col = self.row9.index(empty)

        if row == 0:
            return None
        else:
            return (row, col)

# check if board successfully solved
    def check_board(self):
        for cell in self.cells_to_check:
            correct = 0
            answer = 0
            count = 0
            correctCount = 0

            if self.difficulty == 30:
                correctCount = 30
            elif self.difficulty == 40:
                correctCount = 40
            elif self.difficulty == 50:
                correctCount = 50

            for cell in self.cells_to_check:
                row = cell.get_row()
                col = cell.get_col()
                location = str(row) + str(col)
                ans = self.trueValues[location]
                if ans == cell.get_sketched_value():
                    count += 1

            if count == correctCount:
                return True
            else:
                return False
import pygame

from SudokuGenerator import SudokuGenerator

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False # to indicate if cell is selected
        self.font = pygame.font.Font(None, 36) # font
        self.cell_size = 50 # cell size

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        # stuff for sketching the value inside
        pass

    def draw(self):
        # reference draw_chips() function in main_gui.py
        # reference oop_main.py file

        x = self.col * self.cell_size
        y = self.row * self.cell_size
        rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

        # Draw cell background
        pygame.draw.rect(self.screen, (255, 255, 255), rect)

        # Draw cell outline if selected
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), rect, 3)

        # Draw cell value if not zero
        if self.value != 0:
            text_surface = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        self.generator = SudokuGenerator(width, height)
        self.board = self.generator.get_board()

    def draw(self):
        cell_size = 50
        for i in range(self.width + 1):
            if i % 3 == 0:
                pygame.draw.line(self.screen, BLACK, (i * cell_size, 0), (i * cell_size, self.height * cell_size), 3)
            else:
                pygame.draw.line(self.screen, GRAY, (i * cell_size, 0), (i * cell_size, self.height * cell_size))

        for j in range(self.height + 1):
            if j % 3 == 0:
                pygame.draw.line(self.screen, BLACK, (0, j * cell_size), (self.width * cell_size, j * cell_size), 3)
            else:
                pygame.draw.line(self.screen, GRAY, (0, j * cell_size), (self.width * cell_size, j * cell_size))

        font = pygame.font.Font(None, 36)
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] != 0:
                    text = font.render(self.board[i][j], True, (0, 0, 0))
                    text_rect = text.get_rect(center = ((j*cell_size) + cell_size//2, (i*cell_size) + cell_size//2))
                    self.screen.blit(text, text_rect)

    def select(self, row, col):
        self.selected_cell = (row, col)

    def click(self, x, y):
        cell_size = 50
        col = x // cell_size
        row = y // cell_size

        if 0 <= row < self.height and 0 <= col < self.width:
            return row, col
        else:
            return None

    def clear(self):
        if self.selected_cell is not None:
            row, col = self.selected_cell
            if self.board[row][col] == 0:
                return
            else:
                if self.is_user_filled(row, col):   # might need to fix, def is_user_filled(self, row, col)
                    self.board[row][col] = 0

    def sketch(self, value):
        if self.selected_cell is not None:
            row, col = self.selected_cell
            self.sketches[row][col] = value

    def place_number(self, value):
        if self.selected_cell is not None:
            row, col = self.selected_cell
            self.board[row][col] = value

    def reset_to_original(self):
        for row in range(self.width):
            for col in range(self.height):
                self.board[row][col] = self.original_board[row][col]

    def is_full(self):
        for row in range(self.width):
            for col in range(self.height):
                if self.board[row][col] == 0:
                    return False
        return True

    def update_board(self):
        for row in range(self.width):
            for col in range(self.height):
                self.board[row][col] = self.cells[row][col].get_value()

    def find_empty(self):
        for row in range(self.width):
            for col in range(self.height):
                if self.board[row][col] == 0:
                    return row, col
        return None, None

    def check_board(self):
        for row in range(self.width):
            for col in range(self.height):
                if self.board[row][col] == 0:
                    return False
                # need to add ?

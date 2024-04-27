import pygame
from SudokuGenerator import *
from SudokuBoard import *

# constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CELL_SIZE = 50
GRID_SIZE = 9
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
EASY = 30
MEDIUM = 40
HARD = 50


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku Game Start")

# Font for button text
font = pygame.font.Font(None, 36)

def draw_buttons():
    easy_button_rect = pygame.Rect(175, 150, BUTTON_WIDTH, BUTTON_HEIGHT)
    medium_button_rect = pygame.Rect(175, 250, BUTTON_WIDTH, BUTTON_HEIGHT)
    hard_button_rect = pygame.Rect(175, 350, BUTTON_WIDTH, BUTTON_HEIGHT)

    pygame.draw.rect(screen, (0, 255, 0), easy_button_rect)
    pygame.draw.rect(screen, (255, 255, 0), medium_button_rect)
    pygame.draw.rect(screen, (255, 0, 0), hard_button_rect)

    easy_text = font.render("Easy", True, (0, 0, 0))
    medium_text = font.render("Medium", True, (0, 0, 0))
    hard_text = font.render("Hard", True, (0, 0, 0))

    screen.blit(easy_text, easy_button_rect.center)
    screen.blit(medium_text, medium_button_rect.center)
    screen.blit(hard_text, hard_button_rect.center)


def draw_board(screen, board):
    cell_font = pygame.font.Font(None, 36)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            cell_value = str(board[i][j]) if board[i][j] != 0 else ""
            cell_text = cell_font.render(cell_value, True, BLACK)
            cell_rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, cell_rect)
            screen.blit(cell_text, cell_rect.center)


def main():
    running = True
    selected_difficulty = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    if 175 <= x <= 325 and 150 <= y <= 200:
                        selected_difficulty = EASY
                    elif 175 <= x <= 325 and 250 <= y <= 300:
                        selected_difficulty = MEDIUM
                    elif 175 <= x <= 325 and 350 <= y <= 400:
                        selected_difficulty = HARD

        screen.fill((255, 255, 255))
        draw_buttons()
        pygame.display.flip()

        if selected_difficulty is not None:
            # Generate Sudoku board based on selected difficulty
            sudoku_board = draw_board(selected_difficulty)
            print(sudoku_board)

            # Add code to display selected difficulty board here
            # need to figure out how to use SudokuGenerator Class and cell / board classes for this


    pygame.quit()

if __name__ == "__main__":
    main()

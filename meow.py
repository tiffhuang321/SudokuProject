import pygame, sys
from SudokuGenerator import *
from SudokuBoard import *

pygame.init()  # initialize display
screen = pygame.display.set_mode((450, 500))  # width, height
pygame.display.set_caption("Sudoku")
num_font = pygame.font.Font(None, 60)  # font of numbers
board = generate_sudoku(9, 30)
board[4][3] = "4"
board[3][8] = "5"

def draw_grid():
    # draw horizontal lines
    for i in range(1, 10):
        if i % 3 == 0:
            pygame.draw.line(screen, (100, 165, 150), (0, i*50), (600, i*50), 3)
        else:
            pygame.draw.line(screen, (100, 165, 150), (0, i * 50), (600, i * 50), 1)

    # draw vertical lines
    for i in range(1, 9):
        if i % 3 == 0:
            pygame.draw.line(screen, (100, 165, 150), (i*50, 0), (i*50, 450), 3)
        else:
            pygame.draw.line(screen, (100, 165, 150), (i * 50, 0), (i*50, 450), 1)

def draw_nums():
   num_4_surf = num_font.render("4", 0, (255, 40, 67))
   num_5_surf = num_font.render("5", 0, (5, 40, 67))

   for row in range(9):
       for col in range(9):
           if board[row][col] == "4":
                num_rect = num_4_surf.get_rect(center=(col*50 + 25, row*50 + 28))
                screen.blit(num_4_surf, num_rect)
           elif board[row][col] == "5":
                num_rect = num_5_surf.get_rect(center=(col*50 + 25, row*50 + 28))
                screen.blit(num_5_surf, num_rect)

screen.fill((225, 250, 245))  # choose background color
visual = Board(450, 450, screen, "easy")
draw_grid()
game_over = False
draw_nums()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quitting game w/out error
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // 50
            col = x // 50
            print(x, y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:

    pygame.display.update()
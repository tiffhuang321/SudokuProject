# imports
import pygame
import sys
from SudokuBoard import *
from SudokuGenerator import *


# initialize
pygame.init()

# global vars
difficulty = 0

# main
def game_start(welcomeScreen):
    global difficulty

    # initialize pygame window - 450 x 450 - name it

    # start screen + welcome
    welcomeScreen.fill("lightYellow")
    welcomeFont = pygame.font.Font(None, 50)

    # welcome button
    welcome = welcomeFont.render("Welcome to Sudoku", True, "black")
    welcomeRect = welcome.get_rect()
    welcomeRect.centerx = 630 // 2
    welcomeRect.centery = 180
    welcomeScreen.blit(welcome, welcomeRect)

    difficultyFont = pygame.font.Font(None, 50)


    # easy button
    easy = difficultyFont.render("EASY", True, "black", "white")
    easyRect = easy.get_rect()
    easyRect.centerx = 630 // 2 - 180
    easyRect.centery = 300
    welcomeScreen.blit(easy, easyRect)

    # medium button
    medium = difficultyFont.render("MEDIUM", True, "black", "white")
    mediumRect = medium.get_rect()
    mediumRect.centerx = 630 // 2
    mediumRect.centery = 300
    welcomeScreen.blit(medium, mediumRect)

    hard = difficultyFont.render("HARD", True, "black", "white")
    hardRect = hard.get_rect()
    hardRect.centerx = 630 // 2 + 180
    hardRect.centery = 300
    welcomeScreen.blit(hard, hardRect)

    while True:
        for event in pygame.event.get():
            # if Xed out, quit
            if event.type == pygame.QUIT:
                sys.exit()
            # if mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse clicks easy button
                if easyRect.collidepoint(event.pos):
                    difficulty = 30
                    return
                # if mouse clicks medium button
                elif mediumRect.collidepoint(event.pos):
                    difficulty = 40
                    return
                # if mouse clicks hard button
                elif hardRect.collidepoint(event.pos):
                    difficulty = 50
                    return
        pygame.display.update()


# win game screen
def display_win(screen):
    screen.fill("green")

    winFont = pygame.font.Font(None, 75)
    winMessage = winFont.render("Game Won!", True, "black")
    winRect = winMessage.get_rect()
    winRect.centerx = 225
    winRect.centery = 180
    screen.blit(winMessage, winRect)

# lose game screen
def display_lose(screen):
    red = (255, 158, 158)
    screen.fill(red)

    loseFont = pygame.font.Font(None, 75)
    loseMessage = loseFont.render("You lose!", True, "black")
    loseRect = loseMessage.get_rect()
    loseRect.centerx = 225
    loseRect.centery = 180
    screen.blit(loseMessage, loseRect)


def main():
    # difficulty variable
    global difficulty

    # create screen
    screen = pygame.display.set_mode((630, 630))
    pygame.display.set_caption("Sudoku Game")

    # call game start function - get difficulty value
    game_start(screen)
    print(difficulty) # FOR TESTING PURPOSES ONLY

    # create board with difficulty level + sudoku_generator
    # print board with proper amount of removed difficulty values

    board = Board(630, 630, screen, difficulty)
    board.draw()

    # keep board running loop

    while True:
        for event in pygame.event.get():

            # if Xed out, quit
            if event.type == pygame.QUIT:
                pygame.quit()

            # if mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # set x and y to mouse position
                x, y = event.pos
                # row and col set from x and y
                # redraw the board each time the user selects a cell to redraw the cell's rectangle
                board.draw()
                board.click(x, y)
            # if key press
            if event.type == pygame.KEYDOWN:
                for i in range(1, 10):
                # set num = to the number input
                    if event.unicode == str(i):
                        current_value = i
                        board.sketch(i)
                if event.key == pygame.K_RETURN:
                    board.place_number()
                    board.draw()
                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    board.draw()
                if event.key == pygame.K_c:
                    board.reset_to_original()
                    board.draw()

                '''
                NOTE: check_board function not yet implemented
                '''

                # set the selected cell sketched value = to the user input
                # draw the sketched cell

                # check if the board is full
                if board.is_full():
                    print(111)
                    if board.check_board():
                        print(222)
                        display_win(screen)
                        #pygame.quit()
                    else:
                        print(333)
                        display_lose(screen)
                        #pygame.quit()
                else:
                    print(444)

        pygame.display.update()


# run main
if __name__ == '__main__':
    main()

















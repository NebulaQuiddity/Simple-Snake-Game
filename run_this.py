import pygame
import sys
import json
from pygame.locals import *
import snake_screen as ss
from snake_photos import *
from random import randint

#initialize pygame functions
pygame.init()

#screen dimensions
width = 1319
height = 824

with open('game_data/gamestate.txt', 'w') as gamestate:
    gamestate.write('False')

#main screen
screen = pygame.display.set_mode((width, height))

#a variable for storing new events
new_event = 'still'

#colors used
GRID_COLOR = (60, 60, 60)
BLACK = (0, 0, 0)
GREEN = (0, 240, 0)

#a varaible to see if the player has started playing the game
gamemode = 0

#set caption
pygame.display.set_caption('Snake')

#snake constants
SQUARE_SIZE = 32

new_x = randint(9, 31)
new_y = randint(6, 19)

main_board = ss.SnakeScreen(SQUARE_SIZE, BLACK, GRID_COLOR, screen,
                            height, width, new_x, new_y)


def snake_main(keystroke):
    #game fps
    clock = pygame.time.Clock()
    FPS = 13

    coinstate = False
    coincycle = 0


    with open('game_data/gamestate.txt', 'w') as gamestate:
        gamestate.write('True')

    with open('game_data/add_pieces.txt', 'w') as piece_state:
        piece_state.write('True')

    with open('game_data/apple_state.txt', 'w') as apple_doc:
        apple_doc.write('True')

    while(True):
        cycle = int(FPS / 3)
        if (coincycle >= cycle and coincycle < cycle * 2):
            if coinstate == True:
                coinstate = False
            else:
                coinstate = True
            coincycle += 1
        elif (coincycle >= cycle * 2 and coincycle <= FPS):
            if coinstate == True:
                coinstate = False
            else:
                coinstate = True
            coincycle += 1
        elif (coincycle > FPS):
            if coinstate == True:
                coinstate = False
            else:
                coinstate = True
            coincycle = 0

        else:
            if coinstate == True:
                coinstate = False
            else:
                coinstate = True
            coincycle += 1

        probability = randint(1, 100)
        if (probability == 74):
            with open('game_data/coin_state.txt', 'r') as coin_state:
                has_coin = coin_state.read()
                if has_coin == 'False':

                    with open('game_data/coin_state.txt', 'w') as coin_side:
                        coin_side.write('True')

        main_board.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    keystroke = 'up'
                if event.key == pygame.K_DOWN:
                    keystroke = 'down'
                if event.key == pygame.K_LEFT:
                    keystroke = 'left'
                if event.key == pygame.K_RIGHT:
                    keystroke = 'right'

        with open('game_data/gamestate.txt', 'r') as gamestate:
            running = gamestate.read()
            if (running == 'True'):
                main_board.game_running(keystroke, coinstate)
            else:
                break
        pygame.display.update()

        clock.tick(FPS)



snake_main(new_event)
print(main_board.score)
print('coins = ' + str(main_board.coins))
pygame.quit()
sys.exit()

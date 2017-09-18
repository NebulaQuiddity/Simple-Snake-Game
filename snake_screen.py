import pygame
from snake_photos import *
from random import randint

snake_pieces = []

#colors used
GRID_COLOR = (60, 60, 60)
BLACK = (0, 0, 0)
GREEN = (0, 240, 0)


class SnakeScreen():

    def __init__(self, square_size, screen_color, grid_color,
                screen, height, width, piece_x, piece_y):
        self.square_size = square_size
        self.screen_color = screen_color
        self.grid_color = grid_color
        self.screen = screen
        self.height = height
        self.width = width
        self.apple_x = 0
        self.apple_y = 0
        self.piece_x = piece_x
        self.piece_y = piece_y
        self.piece_type = 'blob'
        self.order = 1
        self.movement = 'still'
        self.pieces = snake_pieces
        self.score = 0
        self.coins = 0
        self.coin_x = None
        self.coin_y = None

        self.square = self.square_size + 1


    def draw_grid(self):
        ''' creates the grid lines on the whole screen, as long with the
            background.                                                 '''

        self.screen.fill(BLACK)

        #draws the vertical lines
        for x in range(self.square_size, self.width - self.square_size,
                        self.square_size + 1):
            pygame.draw.line(self.screen, self.grid_color,
                            (x, 0), (x, self.height))

        #draws the horizontal lines
        for y in range(self.square_size, self.width - self.square_size,
                        self.square_size + 1):
            pygame.draw.line(self.screen, self.grid_color,
                            (0, y), (self.width, y))

    def print_apple(self, apple_state, pieces):
        if (apple_state == 'True'):
            need_apple = True
            while(need_apple):
                self.apple_x = randint(1, 39)
                self.apple_y = randint(1, 24)
                for piece in pieces:
                    if (piece[3] == self.apple_x and piece[4] == self.apple_y):
                        break
                    else:
                        need_apple = False

            with open('game_data/apple_state.txt', 'w') as apple_doc:
                apple_doc.write('False')

        apple_x_pix = (33 * self.apple_x)
        apple_y_pix = (33 * self.apple_y)

        self.screen.blit(apple, (apple_x_pix, apple_y_pix))

    def print_coin(self, coin_state, pieces, coin_side):
        if (coin_state == 'True'):
            if (self.coin_x == None and self.coin_y == None):
                need_coin = True
                while(need_coin):
                    self.coin_x = randint(1, 39)
                    self.coin_y = randint(1, 24)
                    for piece in pieces:
                        if (piece[3] == self.coin_x and piece[4] == self.coin_y):
                            break
                        else:
                            need_coin = False

            with open('game_data/coin_state.txt', 'w') as coin_doc:
                coin_doc.write('False')
        if (self.coin_x != None and self.coin_y != None):
            coin_x_pix = (33 * self.coin_x)
            coin_y_pix = (33 * self.coin_y)

            if (coin_side == True):
                self.screen.blit(coin2, (coin_x_pix, coin_y_pix))
            else:
                self.screen.blit(coin1, (coin_x_pix, coin_y_pix))
    def eat_coin(self, pieces):

        for piece in pieces:
            if (piece[3] == self.coin_x and
                piece[4] == self.coin_y):
                self.coins += 1
                self.coin_x = None
                self.coin_y = None

    def eat_apple(self, pieces):
        for piece in pieces:
            if (piece[3] == self.apple_x and
                piece[4] == self.apple_y):

                if (pieces[-1][2] == 'up'):
                    self.movement = 'up'
                    self.piece_x = pieces[-1][3]
                    self.piece_y = pieces[-1][4] + 1
                    self.piece_type = 'tail'
                    self.order = len(pieces) + 1
                    with open('game_data/add_pieces.txt', 'w') as piece_state:
                        piece_state.write('True')

                if (pieces[-1][2] == 'down'):
                    self.movement = 'down'
                    self.piece_x = pieces[-1][3]
                    self.piece_y = pieces[-1][4] - 1
                    self.piece_type = 'tail'
                    self.order = len(pieces) + 1
                    with open('game_data/add_pieces.txt', 'w') as piece_state:
                        piece_state.write('True')

                if (pieces[-1][2] == 'left'):
                    self.movement = 'left'
                    self.piece_x = pieces[-1][3] + 1
                    self.piece_y = pieces[-1][4]
                    self.piece_type = 'tail'
                    self.order = len(pieces) + 1
                    with open('game_data/add_pieces.txt', 'w') as piece_state:
                        piece_state.write('True')

                if (pieces[-1][2] == 'right'):
                    self.movement = 'right'
                    self.piece_x = pieces[-1][3] - 1
                    self.piece_y = pieces[-1][4]
                    self.piece_type = 'tail'
                    self.order = len(pieces) + 1
                    with open('game_data/add_pieces.txt', 'w') as piece_state:
                        piece_state.write('True')

                with open('game_data/apple_state.txt', 'w') as apple_doc:
                    apple_doc.write('True')

    def update_position(self, event, pieces):
        piece2x = 300
        piece2y = 300
        if (event != 'still'):
            if (len(pieces) > 1):
                for x in range(len(pieces) - 1):
                    if (len(pieces) >= 2):
                        piece2x = pieces[-(x + 1)][3]
                        piece2y = pieces[-(x + 1)][4]

                    #change the x and y to the x and y of the piece infront
                    pieces[-(x + 1)][3] = pieces[-(x + 2)][3]
                    pieces[-(x + 1)][4] = pieces[-(x + 2)][4]

                    #change the direction to the direction of the piece in front
                    pieces[-(x + 1)][2] = pieces[-(x + 2)][2]

        if (event == 'still'):
            pass
        elif (event == 'up'):
            #decrease the y coordinate by one
            if (pieces[0][4] > 0):
                pieces[0][4] -= 1
                pieces[0][2] = 'up'
                if (pieces[0][4] == piece2y):
                    if (pieces[0][4] < 24):
                        pieces[0][4] += 2
                        pieces[0][2] = 'down'
                    else:
                        pieces[0][4] = 'wall'
            else:
                pieces[0][4] = 'wall'
        elif (event == 'down'):
            #increase the y coordinate by one
            if (pieces[0][4] < 24):
                pieces[0][4] += 1
                pieces[0][2] = 'down'
                if (pieces[0][4] == piece2y):
                    if (pieces[0][4] > 0):
                        pieces[0][4] -= 2
                        pieces[0][2] = 'up'
                    else:
                        pieces[0][4] = 'wall'
            else:
                pieces[0][4] = 'wall'
        elif (event == 'left'):
            #decrease the x coordinate by one
            if (pieces[0][3] > 0):
                pieces[0][3] -= 1
                pieces[0][2] = 'left'
                if (pieces[0][3] == piece2x):
                    if (pieces[0][3] < 39):
                        pieces[0][3] += 2
                        pieces[0][2] = 'right'
                    else:
                        pieces[0][3] = 'wall'
            else:
                pieces[0][3] = 'wall'
        elif (event == 'right'):
            #increase the x coordinate by one
            if (pieces[0][3] < 39):
                pieces[0][3] += 1
                pieces[0][2] = 'right'
                if (pieces[0][3] == piece2x):
                    if (pieces[0][3] > 0):
                        pieces[0][3] -= 2
                        pieces[0][2] = 'left'
                    else:
                        pieces[0][3] = 'wall'
            else:
                pieces[0][3] = 'wall'

    def assign_roles(self, pieces):

        if (len(pieces) > 1 and len(pieces) < 3):
            #2 pieces
            pieces[1][1] = 'tail'
            pieces[0][1] = 'head'

        elif (len(pieces) > 1):
            pieces[0][1] = 'head'
            pieces[-1][1] = 'tail'

            for x in range(1, len(pieces) - 1):
                if ((pieces[x][3] < pieces[x + 1][3] and
                    pieces[x][4] > pieces[x - 1][4]) or
                    (pieces[x][3] < pieces[x - 1][3] and
                    pieces[x][4] > pieces[x + 1][4])):

                    pieces[x][1] = 'L1'

                elif ((pieces[x][3] < pieces[x + 1][3] and
                    pieces[x][4] < pieces[x - 1][4]) or
                    (pieces[x][3] < pieces[x - 1][3] and
                    pieces[x][4] < pieces[x + 1][4])):

                    pieces[x][1] = 'L2'

                elif ((pieces[x][3] > pieces[x + 1][3] and
                    pieces[x][4] < pieces[x - 1][4]) or
                    (pieces[x][3] > pieces[x - 1][3] and
                    pieces[x][4] < pieces[x + 1][4])):

                    pieces[x][1] = 'L3'

                elif ((pieces[x][3] > pieces[x + 1][3] and
                    pieces[x][4] > pieces[x - 1][4]) or
                    (pieces[x][3] > pieces[x - 1][3] and
                    pieces[x][4] > pieces[x + 1][4])):

                    pieces[x][1] = 'L4'
                else:
                    pieces[x][1] = 'body'

    def coordinate_tail(self, pieces):
        tail_x = pieces[-1][3]
        tail_y = pieces[-1][4]

        if len(pieces) > 1:
            if (tail_x > pieces[-2][3]):
                pieces[-1][2] = 'left'
            elif (tail_x < pieces[-2][3]):
                pieces[-1][2] = 'right'
            elif (tail_y < pieces[-2][4]):
                pieces[-1][2] = 'down'
            elif (tail_y > pieces[-2][4]):
                pieces[-1][2] = 'up'




    def print_snake(self, pieces, screen):

        for piece in pieces:
            x_pixels = (33 * piece[3])
            y_pixels = (33 * piece[4])

            if (piece[1] == 'blob'):
                try:
                    screen.blit(snake_blob, (x_pixels, y_pixels))
                except TypeError:
                    print('game has ended')
                    with open('game_data/gamestate.txt', 'w') as gamestate:
                        gamestate.write('False')

            elif (piece[1] == 'head'):
                if (piece[2] == 'up'):
                    try:
                        screen.blit(snake_head_up, (x_pixels, y_pixels))
                    except TypeError:
                        print('game has ended')
                        with open('game_data/gamestate.txt', 'w') as gamestate:
                            gamestate.write('False')
                if (piece[2] == 'down'):
                    try:
                        screen.blit(snake_head_down, (x_pixels, y_pixels))
                    except TypeError:
                        print('game has ended')
                        with open('game_data/gamestate.txt', 'w') as gamestate:
                            gamestate.write('False')
                if (piece[2] == 'left'):
                    try:
                        screen.blit(snake_head_left, (x_pixels, y_pixels))
                    except TypeError:
                        print('game has ended')
                        with open('game_data/gamestate.txt', 'w') as gamestate:
                            gamestate.write('False')
                if (piece[2] == 'right'):
                    try:
                        screen.blit(snake_head_right, (x_pixels, y_pixels))
                    except TypeError:
                        print('game has ended')
                        with open('game_data/gamestate.txt', 'w') as gamestate:
                            gamestate.write('False')


            elif (piece[1] == 'body'):
                if (piece[2] == 'up'):
                        screen.blit(snake_body_up, (x_pixels, y_pixels))
                if (piece[2] == 'down'):
                        screen.blit(snake_body_down, (x_pixels, y_pixels))
                if (piece[2] == 'left'):
                        screen.blit(snake_body_left, (x_pixels, y_pixels))
                if (piece[2] == 'right'):
                        screen.blit(snake_body_right, (x_pixels, y_pixels))


            elif (piece[1] == 'L1'):
                screen.blit(snake_corner_L1, (x_pixels, y_pixels))
            elif (piece[1] == 'L2'):
                screen.blit(snake_corner_L2, (x_pixels, y_pixels))
            elif (piece[1] == 'L3'):
                screen.blit(snake_corner_L3, (x_pixels, y_pixels))
            elif (piece[1] == 'L4'):
                screen.blit(snake_corner_L4, (x_pixels, y_pixels))


            elif (piece[1] == 'tail'):
                if (piece[2] == 'up'):
                        screen.blit(snake_tail_up, (x_pixels, y_pixels))
                if (piece[2] == 'down'):
                        screen.blit(snake_tail_down, (x_pixels, y_pixels))
                if (piece[2] == 'left'):
                        screen.blit(snake_tail_left, (x_pixels, y_pixels))
                if (piece[2] == 'right'):
                        screen.blit(snake_tail_right, (x_pixels, y_pixels))


    def game_running(self, keystroke, coincycle, pieces = snake_pieces):
        ''' starts the game with the character on the grid. x and y are
            not in pixels, but in grid coordinates                     '''

        with open('game_data/apple_state.txt', 'r') as apple_doc:
            apple_state = apple_doc.read()

        with open('game_data/add_pieces.txt', 'r') as piece_state:
            piecebool = piece_state.read()

        if (piecebool == 'True'):
            pieces.append([self.order, self.piece_type, self.movement,
                        self.piece_x, self.piece_y])

        self.print_apple(apple_state, pieces)

        with open('game_data/coin_state.txt', 'r') as coin_doc:
            coin_state = coin_doc.read()

        self.print_coin(coin_state, pieces, coincycle)

        with open('game_data/add_pieces.txt', 'w') as piece_state:
                piece_state.write('False')

        self.update_position(keystroke, snake_pieces)

        #stop the game if the player has run into a wall
        if (len(pieces) > 0):
            if (pieces[0][4] == 'wall' or pieces[0][3] == 'wall'):
                with open('game_data/gamestate.txt', 'w') as gamestate:
                    gamestate.write('False')
                    print('game has ended, player has run into a wall!')
            else:

                self.eat_apple(pieces)

                self.eat_coin(pieces)

                self.assign_roles(pieces)

                self.coordinate_tail(pieces)

                self.print_snake(pieces, self.screen)



        #stop the game if the player has run into themselves
        if (len(pieces) > 1):
            for piece in pieces[2:]:
                if (pieces[0][3] == piece[3] and pieces[0][4] == piece[4]):
                    with open('game_data/gamestate.txt', 'w') as gamestate:
                        gamestate.write('False')
                        print('game has ended, player has run into themselves!')

        self.score = len(pieces)

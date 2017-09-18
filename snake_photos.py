import pygame

#snake images (includes separate images for each 4 permutations)
snake_head_up = pygame.image.load('game_data/images/snake_head_up.png')
snake_head_down = pygame.image.load('game_data/images/snake_head_down.png')
snake_head_left = pygame.image.load('game_data/images/snake_head_left.png')
snake_head_right = pygame.image.load('game_data/images/snake_head_right.png')

snake_body_up = pygame.image.load('game_data/images/snake_body_up.png')
snake_body_left = pygame.image.load('game_data/images/snake_body_left.png')
snake_body_right = pygame.image.load('game_data/images/snake_body_right.png')
snake_body_down = pygame.image.load('game_data/images/snake_body_down.png')

snake_tail_up = pygame.image.load('game_data/images/snake_tail_up.png')
snake_tail_down = pygame.image.load('game_data/images/snake_tail_down.png')
snake_tail_left = pygame.image.load('game_data/images/snake_tail_left.png')
snake_tail_right = pygame.image.load('game_data/images/snake_tail_right.png')

#L1 is a corner in the shape of an l, the rest are sequential clocwise
#rotations of that
snake_corner_L1 = pygame.image.load('game_data/images/snake_corner_L1.png')
snake_corner_L2 = pygame.image.load('game_data/images/snake_corner_L2.png')
snake_corner_L3 = pygame.image.load('game_data/images/snake_corner_L3.png')
snake_corner_L4 = pygame.image.load('game_data/images/snake_corner_L4.png')

snake_blob = pygame.image.load('game_data/images/snake_blob.png')



#things to pick up during game
apple = pygame.image.load('game_data/images/snake_apple.png')
coin1 = pygame.image.load('game_data/images/coin1.png')
coin2 = pygame.image.load('game_data/images/coin2.png')

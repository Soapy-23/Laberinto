import pygame as pg

WINDOW_WIDTH = 800
WINDOW_WIDHT = 800
WINDOW_HEIGHT = 600

POS_X = 100
POS_Y = 100
SPEED = 7
WIDTH_PLAYER = 50
HEIGHT_PLAYER = 50
CELL_SIZE = 20

BACKGROUND = pg.image.load('assetes/ground.jpg')
BACKGROUND = pg.transform.scale(BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))

IMG_VICTORY = pg.image.load('assetes/youwin.jpg')
IMG_VICTORY = pg.transform.scale(IMG_VICTORY, (WINDOW_WIDTH, WINDOW_HEIGHT))

IMG_LOSER = pg.image.load('assetes/youdied.jpg')
IMG_LOSER = pg.transform.scale(IMG_LOSER, (WINDOW_WIDTH, WINDOW_HEIGHT))


PLAYER_IMAGES = {
    'DOWN': [
        'assetes/player/p_down_01.png',
        'assetes/player/p_down_02.png',
        'assetes/player/p_down_03.png', 
        'assetes/player/p_down_04.png'
    ],
    'UP': [
        'assetes/player/p_up_01.png',
        'assetes/player/p_up_02.png',
        'assetes/player/p_up_03.png', 
        'assetes/player/p_up_04.png'
    ],
    'LEFT': [
        'assetes/player/p_left_01.png',
        'assetes/player/p_left_02.png',
        'assetes/player/p_left_03.png', 
        'assetes/player/p_left_04.png'
    ],
    'RIGHT': [
        'assetes/player/p_right_01.png',
        'assetes/player/p_right_02.png',
        'assetes/player/p_right_03.png', 
        'assetes/player/p_right_04.png'
    ]
}

WALL_IMAGE = 'assetes/wall.png'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

COLORS = {
    'red': RED,
    'green': GREEN,
    'blue': BLUE,
    'yellow': YELLOW,
    'white': WHITE,
    'black': BLACK,
}


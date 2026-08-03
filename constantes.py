import pygame as pg

WINDOW_WIDHT = 800
WINDOW_HEIGHT = 600

POS_X = 100
POS_Y = 100
SPEED = 7
WIDTH_PLAYER = 20
HEIGHT_PLAYER = 20


BACKGROUND = pg.image.load('assets/background.png')
BACKGROUND = pg.transform.scale(BACKGROUND, (WINDOW_WIDHT, WINDOW_HEIGHT))

IMG_VICTORY = pg.image.load('assets/victoria.png')
IMG_VICTORY = pg.transform.scale(IMG_VICTORY, (WINDOW_WIDHT, WINDOW_HEIGHT))

IMG_LOSER = pg.image.load('assets/derrota.png')
IMG_LOSER = pg.transform.scale(IMG_LOSER, (WINDOW_WIDHT, WINDOW_HEIGHT))


PLAYER_IMAGES = {
    'DOWN': [
        'assets/player/down_0.png',
        'assets/player/down_1.png',
        'assets/player/down_2.png'
    ],
    'UP': [
        'assets/player/up_0.png',
        'assets/player/up_1.png',
        'assets/player/up_2.png'
    ],
    'LEFT': [
        'assets/player/left_0.png',
        'assets/player/left_1.png',
        'assets/player/left_2.png'
    ],
    'RIGHT': [
        'assets/player/right_0.png',
        'assets/player/right_1.png',
        'assets/player/right_2.png'
    ]
}

WALL_IMAGE = 'assets/wall.png'

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
}


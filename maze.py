import pygame as pg
import constantes as c
from clases import Wall, Player

MAZE_LAYOUT = [
    'WWWWWWWWWWWW',
    'W    P     W',
    'W  W   W   W',
    'W  W   W   W',
    'W     E    W',
    'W         WW',
    'W  W  W W  W'
    'W  W   W W W'
    'W  W   W W W'
    'W  W   W   W'
    'W  W   W W W'
    'W  W   W W W'
    'W  W   W W W'
    'W  W   W   W'
    'W  W   W   W'
    'W WWWWWWWWWW'
]

class Level:
    def __init__(self, layout, walls_group, all_sprites_group, player_group):
        self.layout = layout
        self.walls_group = walls_group
        self.all_sprites_group = all_sprites_group
        self.player_group = player_group
        self.load_level()
    
    def load_level(self):
        for y, fila in enumerate(self.layout):
            for x, char in enumerate(fila):
                if char == 'W':
                    wall = Wall(x * c.CELL_SIZE, y * c.CELL_SIZE, c.CELL_SIZE, c.CELL_SIZE)
                    self.walls_group.add(wall)
                    self.all_sprites_group.add(wall)
                if char == 'P':
                    self.player = Player(x * c.CELL_SIZE, y * c.CELL_SIZE, self.walls_group)
                    self.player_group.add(self.player)
                    self.all_sprites_group.add(self.player)
                if char == 'E':
                    self.enemy = Enemy(x * c.CELL_SIZE, y * c.CELL_SIZE, self.walls_group)
                    self.enemy_group.add(self.enemy)
                    self.all_sprites_group.add(self.enemy)

    def run(self, surface):
        self.all_sprites_group.update()
        surface.blit(cons.BACKGROUND, (0, 0))
        self.all_sprites_group.draw(surface)
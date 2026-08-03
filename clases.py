import pygame as pg
import constants as c

class Wall(pg.sprite.Sprite):
    def __init__(self, POS_X, POS_Y, width, height, image_path = None):
        super().__init__()
        if image_path:
            self.image = pg.image.load(image_path)
            self.image = pg.transform.scale(self.image, (width, height))
        else:
            self.image = pg.Surface([width, height])
            self.image.fill(c.BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = POS_X
        self.rect.y = POS_Y

class Player(pg.sprite.Sprite):
    def __init__(self, POS_X, POS_Y, walls_group, img_dict):
        super().__init__()
        self.walls = walls_group
        self.img_dict = self._load_images(img_dict)
        self.direction = 'DOWN'
        self.is_moving = False
        self.frame_count = 0
        self.animation_speed = 5
        self.current_frame = 0
        self.image = self.animations[self.direction][self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = POS_X
        self.rect.y = POS_Y

        self.vel_x = 0
        self.vel_y = 0

    def _load_images(self, img_dict):
        animations = {}
        for directions, paths in img_dict.items():
            animations[directions] = []
            for path in paths:
                surf = pg.image.load(path)
                surf = pg.transform.scale(surf, (c.WIDTH_PLAYER, c.HEIGHT_PLAYER))
                animations[directions].append(surf)
        return animations
    
    def get_input(self):
        keys = pg.key.get_pressed()
        self.vel_x = 0
        self.vel_y = 0
        self.is_moving = False

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel_x = -c.SPEED
            self.is_moving = True
            self.direction = 'LEFT'
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel_x = c.SPEED
            self.is_moving = True
            self.direction = 'RIGHT'
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel_y = -c.SPEED
            self.is_moving = True
            self.direction = 'UP'
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel_y = c.SPEED
            self.is_moving = True
            self.direction = 'DOWN'
    
        self.is_moving = self.vel_x != 0 or self.vel_y != 0

    def animate(self):
        if self.is_moving:
            self.frame_count += 1
            if self.frame_count // self.animation_speed >= len(self.animations[self.direction]):
                self.frame_count = 0
            self.current_frame = self.frame_count // self.animation_speed
            self.image = self.animations[self.direction][self.current_frame]
        else:
            self.current_frame = 0
            self.image = self.animations[self.direction][self.current_frame]
    
    def move_and_collide(self):
        self.rect.x += self.vel_x
        hits = pg.sprite.spritecollide(self, self.walls, False)
        if hits:
            for hit in hits:
                if self.vel_x > 0:
                    self.rect.right = hit.rect.left
                if self.vel_x < 0:
                    self.rect.left = hit.rect.right
        self.rect.y += self.vel_y
        hits = pg.sprite.spritecollide(self, self.walls, False)
        if hits:
            for hit in hits:
                if self.vel_y > 0:
                    self.rect.bottom = hit.rect.top
                else:
                    self.rect.top = hit.rect.bottom
            
    def update(self):
        self.get_input()
        self.animate()
        self.move_and_collide()

class Enemy(pg.sprite.Sprite):
    def __init__(self, POS_X, POS_Y, walls_group):
        super().__init__()
        self.walls = walls_group
        self.image = pg.Surface([c.WIDTH_PLAYER, c.HEIGHT_PLAYER])
        self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = POS_X
        self.rect.y = POS_Y

        self.vel_x = c.SPEED
        self.vel_y = 0
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        hits = pg.sprite.spritecollide(self, self.walls, False)
        if hits:
            for hit in hits:
                if self.vel_x > 0:
                    self.rect.right = hit.rect.left
                if self.vel_x < 0:
                    self.rect.left = hit.rect.right
        hits = pg.sprite.spritecollide(self, self.walls, False)
        if hits:
            for hit in hits:
                if self.vel_y > 0:
                    self.rect.bottom = hit.rect.top
                else:
                    self.rect.top = hit.rect.bottom

            

                

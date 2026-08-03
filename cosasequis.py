import pygame as pg
import time
import sys

pg.init() 

class GameSprite: 
    def __init__(self, x, y, img, speed = 5):
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.speed = speed 

    def draw(self, surface): 
        surface.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite): 
    def move(self): 
        keys = pg.key.get_pressed()
        # Movimiento y colisión en el eje x 
        dx = 0 
        if keys[pg.K_LEFT] and self.rect.x > 0 - self.rect.width: 
            dx -= self.speed 
        if keys[pg.K_RIGHT] and self.rect.x < 800 - self.rect.width: 
            dx += self.speed         
        self.rect.x += dx 

        # Límites de la pantalla en x
        if self.rect.x < 0: 
            self.rect.x = 0
        if self.rect.x > 800 - self.rect.width: 
            self.rect.x = 800 - self.rect.width

        for wall in walls: 
            if self.rect.colliderect(wall.rect): 
                if dx > 0: 
                    self.rect.right = wall.rect.left 
                if dx < 0: 
                    self.rect.left = wall.rect.right 

        # Movimiento y colisión en el eje y
        dy = 0
        if keys[pg.K_UP] and self.rect.y > 0: 
            dy -= self.speed         
        if keys[pg.K_DOWN] and self.rect.y < 600 - self.rect.height: 
            dy += self.speed       
        self.rect.y += dy
        # Límites de la pantalla en y
 
        for wall in walls: 
            if self.rect.colliderect(wall.rect): 
                if dy > 0: 
                    self.rect.bottom = wall.rect.top 
                if dy < 0: 
                    self.rect.top = wall.rect.bottom   

class Wall(GameSprite): 
    def __init__(self, x, y, width, height, color): 
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Mi juego")

wall1 = Wall(50, 50, 300, 50, (0, 255, 0))
wall2 = Wall(50, 250, 50, 200, (0, 255, 0))
wall3 = Wall(150, 250, 50, 150, (0, 255, 0))
wall4 = Wall(250, 250, 250, 50, (0, 255, 0))
wall5 = Wall(50, 500, 250, 50, (0, 255, 0))

walls = [wall1, wall2, wall3, wall4, wall5]

img_Roma = pg.image.load("Roma.png").convert_alpha()
img_Roma = pg.transform.scale(img_Roma, (50, 50))
Roma = Player(100, 100, img_Roma, 5)

clock = pg.time.Clock()
time.sleep(3)

background = pg.image.load("6902fd9830bc8.jpg").convert()
background = pg.transform.scale(background, (800, 600))

goal = GameSprite(750, 550, pg.transform.scale(pg.image.load("youdied.png").convert_alpha(), (50, 50)))

while True: 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            pg.quit()
            sys.exit()


    screen.blit(background, (0, 0))

    if Roma.rect.colliderect(goal.rect): 
        screen.blit(pg.transform.scale(pg.image.load("youdied.png").convert_alpha(), (800, 600)), (0, 0))
        pg.display.update()
        time.sleep(5)
        pg.quit()
        sys.exit()


    for wall in walls: 
        wall.draw(screen)
    
    Roma.move()
    Roma.draw(screen)
    goal.draw(screen)
    pg.display.update()
    clock.tick(60)




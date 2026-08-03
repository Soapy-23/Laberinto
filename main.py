import pygame as pg
import constantes as cons
import sys
import maze

def main():
    pg.init()
    screen = pg.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
    pg.display.set_caption("Maze")
    clock = pg.time.Clock()
    walls_group = pg.sprite.Group()
    all_sprites_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    maze_obj = maze.Level(maze.MAZE_LAYOUT, walls_group, all_sprites_group, player_group)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        maze_obj.run(screen)
        pg.display.flip()
        clock.tick(60)
    pg.quit()
    sys.exit()

if __name__ == '__main__':
    main()
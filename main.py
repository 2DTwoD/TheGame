import pygame
import sys

from characters.enemy import Enemy
from characters.hero import Hero
from other.unit_parameters import Color
from other.glb import Global
from walls.wall import Wall

pygame.init()
clock = pygame.time.Clock()
backgroundColor = Color(0, 0, 0)
glb = Global()
screen = pygame.display.set_mode((500, 500))
hero = Hero(glb, True)
walls = [Wall(400, 400, 100, 100, Color(128, 128, 0), glb),
         Wall(200, 300, 100, 100, Color(128, 128, 0), glb),
         Wall(100, 200, 100, 100, Color(128, 128, 0), glb),
         Wall(0, 100, 100, 100, Color(128, 128, 0), glb),
         Wall(100, 500, 300, 100, Color(128, 128, 0), glb)]

enemies = [Enemy(0, 300, 25, 25, Color(237, 28, 26), glb)]
# Wall(0, 500, 500, 100, Color(128, 128, 0), glb),
#          Wall(200, 400, 100, 100, Color(128, 128, 0), glb)
glb.initGlobal(screen, hero, walls, enemies)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        hero.eventHandler(event)


    for wall in walls:
        wall.draw()
    hero.draw()

    pygame.display.flip()
    screen.fill(backgroundColor.get())
    clock.tick(60)

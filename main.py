import pygame
import sys

from units.enemy import Enemy
from other.unit_parameters import Color
from other.glb import Global
from units.hero import Hero
from units.wall import Wall

pygame.init()
clock = pygame.time.Clock()
backgroundColor = Color(0, 0, 0)
Global.hero = Hero()
Global.walls.extend([Wall(0, 500, 500, 100, Color(128, 128, 0)),
                       Wall(200, 400, 100, 100, Color(128, 128, 0))])

Global.enemies.extend([Enemy(300, 0, 25, 25, Color(237, 28, 36))])
#
# Wall(400, 400, 100, 100, Color(128, 128, 0)),
#                     Wall(200, 300, 100, 100, Color(128, 128, 0)),
#                     Wall(100, 200, 100, 100, Color(128, 128, 0)),
#                     Wall(0, 100, 100, 100, Color(128, 128, 0)),
#                     Wall(100, 500, 300, 100, Color(128, 128, 0))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        Global.hero.eventHandler(event)

    for wall in Global.walls:
        wall.draw()
    for enemy in Global.enemies:
        enemy.draw()
    for bullet in Global.bullets.copy():
        bullet.draw()
    Global.hero.draw()

    pygame.display.flip()
    Global.screen.fill(backgroundColor.get())
    clock.tick(60)

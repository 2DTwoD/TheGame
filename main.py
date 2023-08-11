from random import random, randrange

import pygame
import sys

from units.enemy import Enemy
from other.unit_parameters import Color
from other.glb import Global
from units.hero import Hero
from units.levels import WallCreator
from units.wall import Wall

pygame.init()
clock = pygame.time.Clock()
backgroundColor = Color(0, 0, 0)
Global.hero = Hero()
Global.walls.update([Wall(400, 400, 100, 100, Color(128, 128, 0)),
                    Wall(200, 300, 100, 100, Color(128, 128, 0)),
                    Wall(100, 200, 100, 100, Color(128, 128, 0)),
                    Wall(0, 100, 100, 100, Color(128, 128, 0)),
                    Wall(100, 500, 300, 100, Color(128, 128, 0))])
# Global.walls.update([Wall(0, 450, 500, 100, Color(128, 128, 0)),
#                        Wall(0, 300, 100, 100, Color(128, 128, 0))])

wallCreator = WallCreator()
while True:
    wallCreator.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Global.keys = pygame.key.get_pressed()
    for wall in Global.walls.copy():
        wall.draw()
    for enemy in Global.enemies.copy():
        enemy.draw()
    for bullet in Global.bullets.copy():
        bullet.draw()
    Global.hero.draw()

    pygame.display.flip()
    Global.screen.fill(backgroundColor.get())
    clock.tick(60)


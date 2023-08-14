import pygame
import sys

from other.unit_parameters import Color
from other.glb import Global
from units.hero import Hero
from units.levels import WallCreator
from units.titles import Titles

pygame.init()
clock = pygame.time.Clock()
backgroundColor = Color(0, 0, 0)
Global.hero = Hero()
wallCreator = WallCreator()
Global.titles = Titles()

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
    for bonus in Global.bonuses.copy():
        bonus.draw()
    Global.hero.draw()
    Global.titles.getTitles()
    pygame.display.flip()
    Global.screen.fill(backgroundColor.get())
    clock.tick(60)


import pygame
import sys

from other.unit_parameters import Color
from other.glb import Global
from units.hero import Hero
from units.level_creator import LevelCreator
from units.menu import Menu

pygame.init()
clock = pygame.time.Clock()
backgroundColor = Color(0, 0, 0)
Global.hero = Hero()
Global.levelCreator = LevelCreator()
Global.titles = Menu()


def action(collection: set):
    for obj in collection.copy():
        if Global.gameOver:
            collection.discard(obj)
        else:
            obj.draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Global.keys = pygame.key.get_pressed()

    action(Global.walls)

    if not Global.gameOver:
        Global.levelCreator.run()
        Global.hero.draw()

    action(Global.enemies)
    action(Global.bullets)
    action(Global.bonuses)

    Global.titles.getTitles()

    pygame.display.flip()
    Global.screen.fill(backgroundColor.get())
    clock.tick(60)

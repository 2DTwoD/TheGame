import pygame
import sys

from other.unit_parameters import Colors
from other.glb import Global
from units.hero import Hero
from units.level_creator import LevelCreator
from units.menu import Menu

pygame.init()
clock = pygame.time.Clock()
backgroundColor = Colors.BLACK
Global.hero = Hero()
Global.levelCreator = LevelCreator()
Global.menu = Menu()


def action(collection: set):
    for obj in collection.copy():
        if Global.gameOver:
            collection.discard(obj)
        else:
            obj.draw()


while True:
    for event in pygame.event.get():
        Global.menu.inputTextHandler(event)
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

    Global.menu.getMenu()

    pygame.display.flip()
    Global.screen.fill(backgroundColor)
    clock.tick(Global.FPS)

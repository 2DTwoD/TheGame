import pygame
import sys

from other.unit_parameters import Colors
from other.glb import Global
from units.hero import Hero
from units.level_creator import LevelCreator
from units.menu import Menu

pygame.init()
pygame.display.set_caption('TheGame')
pygame.display.set_icon(pygame.image.load('ico/ico.png'))

clock = pygame.time.Clock()

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

    if not Global.gameOver and not Global.pause:
        Global.levelCreator.run()
        Global.hero.draw()

    action(Global.enemies)
    action(Global.bullets)
    action(Global.bonuses)

    Global.menu.getMenu()

    pygame.display.flip()

    if Global.gameOver or Global.pause:
        backGround = Colors.BLACK
    else:
        backGround = Global.backgroundColors[Global.difficult - 1] if Global.difficult <= len(
            Global.backgroundColors) else Global.backgroundColors[-1]
    Global.screen.fill(backGround)
    clock.tick(Global.FPS)

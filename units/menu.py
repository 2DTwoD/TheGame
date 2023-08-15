from random import randint

import pygame

from other.glb import Global
from other.unit_parameters import Color, Colors


class Menu:
    def __init__(self):
        pygame.font.init()
        self.titleFont = pygame.font.SysFont('Times New Roman', 50)
        self.menuFont = pygame.font.SysFont('Times New Roman', 20)
        self.gameFont = pygame.font.SysFont('Times New Roman', 20)
        self._scores = 0
        self.color = Colors.GRAY

    def getTitles(self):
        if Global.gameOver:
            rainbow = Color(randint(0, 255), randint(0, 255), randint(0, 255))
            x = 2 * Global.screenWidth() / 5
            Global.screen.blit(self.titleFont.render("TheGame", False,  rainbow.get()), (x, 3 * Global.screenHeight() / 10))
            Global.screen.blit(self.menuFont.render("Control:", False, self.color.get()),
                               (x, 8 * Global.screenHeight() / 20))
            Global.screen.blit(self.menuFont.render("A/D - Left/Right", False, self.color.get()),
                               (x, 9 * Global.screenHeight() / 20))
            Global.screen.blit(self.menuFont.render("W - Jump", False, self.color.get()),
                               (x, 10 * Global.screenHeight() / 20))
            Global.screen.blit(self.menuFont.render("SPACE - Shoot", False, self.color.get()),
                               (x, 11 * Global.screenHeight() / 20))
            Global.screen.blit(self.menuFont.render("Push ENTER to start", False, self.color.get()),
                               (x, 12 * Global.screenHeight() / 20))
            if Global.keys[pygame.K_RETURN] and Global.setsIsEmpty():
                Global.gameOver = False
                Global.hero.reInit()
                Global.levelCreator.reInit()
        else:
            Global.screen.blit(self.gameFont.render("Scores: " + str(Global.levelCreator.scores), False, self.color.get()), (0, 0))
            Global.screen.blit(self.gameFont.render("Health: " + str(Global.hero.health), False, self.color.get()), (0, 30))
            Global.screen.blit(self.gameFont.render("Bullets: " + str(Global.hero.bullets), False, self.color.get()), (0, 60))



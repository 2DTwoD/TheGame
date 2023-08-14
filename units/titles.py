import pygame

from other.glb import Global
from other.unit_parameters import Color


class Titles:
    def __init__(self):
        pygame.font.init()
        self.healthFont = pygame.font.SysFont('Comic Sans MS', 30)
        self.scoreFont = pygame.font.SysFont('Comic Sans MS', 30)
        self.bulletFont = pygame.font.SysFont('Comic Sans MS', 30)
        self._scores = 0
        self._bullets = 100
        self.color = Color(255, 255, 255)

    def getTitles(self):
        Global.screen.blit(self.scoreFont.render("Scores: " + str(self.scores), False, self.color.get()), (0, 0))
        Global.screen.blit(self.healthFont.render("Health: " + str(Global.hero.health), False, self.color.get()), (0, 30))
        Global.screen.blit(self.bulletFont.render("Bullets: " + str(self.bullets), False, self.color.get()), (0, 60))

    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, value):
        self._scores = value * Global.difficult

    @property
    def bullets(self):
        return self._bullets

    @bullets.setter
    def bullets(self, value):
        self._bullets = value

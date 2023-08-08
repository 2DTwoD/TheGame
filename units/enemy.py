import pygame

from other.glb import Global
from other.unit_interfaces import GravityUnitI
from other.unit_parameters import Color


class Enemy(GravityUnitI):
    move = 2

    def __init__(self, x, y, width, height, color: Color):
        GravityUnitI.__init__(self, x, y, width, height)
        self.color = color
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))

    def singleEngine(self):
        if self.coordinates.x < Global.hero.coordinates.x - Global.hero.dimensions.x / 2:
            self.speed.x = Enemy.move
        elif self.coordinates.x > Global.hero.coordinates.x + Global.hero.dimensions.x / 2:
            self.speed.x = -Enemy.move
        else:
            self.speed.x = 0
        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)

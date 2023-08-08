import pygame

from other.glb import Global
from other.unit_interfaces import UnitI
from other.unit_parameters import Color


class Bullet(UnitI):
    move = 15

    def __init__(self, x, y, direction):
        UnitI.__init__(self, x, y, 5, 5)
        self.move = -15 if direction != 1 else 15
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.color = Color(255, 255, 255)
        self.delFlag = False

    def singleEngine(self):
        self.coordinates.x += self.move

        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)
        if self.coordinates.x > Global.SCREEN_SIZE[0] or self.coordinates.x < 0:
            Global.bullets.discard(self)

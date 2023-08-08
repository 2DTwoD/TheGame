import pygame

from other.glb import Global
from other.unit_interfaces import WallI
from other.unit_parameters import Color


class Wall(WallI):
    def __init__(self, x, y, width, height, color: Color):
        WallI.__init__(self, x, y, width, height)
        self.color = color
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))

    def singleEngine(self):
        if self.coordinates.y > Global.SCREEN_SIZE[1]:
            self.coordinates.y = - self.dimensions.y
        self.shape.y = self.coordinates.y
        pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)

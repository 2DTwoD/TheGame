import pygame

from other.glb import Global
from other.unit_interfaces import UnitI


class Wall(UnitI):
    def __init__(self, x, y, width, height, color):
        UnitI.__init__(self, x, y, width, height)
        self.color = color
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))

    def singleEngine(self):
        if self.coordinates.y > Global.screenHeight() + 1:
            Global.walls.discard(self)

    def drawFigure(self):
        self.shape.y = self.coordinates.y
        pygame.draw.rect(Global.screen, self.color, self.shape, 0)

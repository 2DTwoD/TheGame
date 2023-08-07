import pygame

from other.unit_interfaces import Unit
from other.unit_parameters import Color


class Wall(Unit):
    def __init__(self, x, y, width, height, color: Color, glb):
        Unit.__init__(self, x, y, width, height)
        self.glb = glb
        self.color = color
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))

    def updateShape(self):
        self.shape.y = self.coordinates.y
        pygame.draw.rect(self.glb.screen, self.color.get(), self.shape, 0)
        if self.coordinates.y > 500:
            self.coordinates.y = - self.dimensions.y


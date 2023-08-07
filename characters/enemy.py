import pygame

from other.unit_interfaces import Unit
from other.unit_parameters import Color

class Enemy(Unit):
    def __init__(self, x, y, width, height, color: Color, glb):
        Unit.__init__(self, x, y, width, height)
        self.color = color
        self.glb = glb
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))

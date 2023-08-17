from random import randint

import pygame


class Pair:
    def __init__(self, _x: int, _y: int):
        self._x = _x
        self._y = _y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    def get(self):
        return self.x, self.y


class Colors:
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)
    GREEN = pygame.Color(34, 117, 76)
    GRAY = pygame.Color(195, 195, 195)
    RED = pygame.Color(237, 28, 36)
    BLUE = pygame.Color(0, 162, 232)
    YELLOW = pygame.Color(255, 242, 0)
    BROWN = pygame.Color(131, 81, 54)

    @staticmethod
    def getRandom():
        return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))

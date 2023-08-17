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
    SKY1 = pygame.Color(51, 216, 189)
    SKY2 = pygame.Color(57, 213, 118)
    SKY3 = pygame.Color(178, 213, 119)
    SKY4 = pygame.Color(152, 219, 205)
    SKY5 = pygame.Color(222, 188, 212)
    SKY6 = pygame.Color(209, 122, 137)
    SKY7 = pygame.Color(138, 93, 98)
    SKY8 = pygame.Color(98, 80, 110)
    SKY9 = pygame.Color(23, 23, 55)
    SKY10 = BLACK
    WALL1 = pygame.Color(0, 59, 94)
    WALL2 = pygame.Color(73, 76, 140)
    WALL3 = pygame.Color(188, 102, 16)
    WALL4 = pygame.Color(36, 78, 56)
    WALL5 = pygame.Color(226, 98, 36)
    WALL6 = pygame.Color(83, 47, 30)
    WALL7 = pygame.Color(86, 27, 57)
    WALL8 = pygame.Color(22, 44, 57)
    WALL9 = pygame.Color(100, 67, 172)
    WALL10 = pygame.Color(67, 93, 105)

    @staticmethod
    def getRandom():
        return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))

    @staticmethod
    def getInverse(color):
        return pygame.Color(255 - color.r, 255 - color.g, 255 - color.b)


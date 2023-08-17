from random import randint

import pygame

from other.glb import Global
from other.unit_interfaces import UnitI
from other.unit_parameters import Colors


class Bonus(UnitI):
    HEALTH = 0
    SCORE = 1
    BULLET = 2

    def __init__(self, x, y):
        UnitI.__init__(self, x, y, 30, 30)
        self.type = randint(0, 2)
        match self.type:
            case Bonus.HEALTH:
                self.color = Colors.GREEN
            case Bonus.SCORE:
                self.color = Colors.YELLOW
            case Bonus.BULLET:
                self.color = Colors.BLUE
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))

    def singleEngine(self):
        if self.coordinates.y > Global.screenHeight():
            Global.bonuses.discard(self)
        if self.hitTest(Global.hero):
            match self.type:
                case Bonus.HEALTH:
                    Global.hero.health += 10
                case Bonus.SCORE:
                    Global.levelCreator.score += 30 * Global.difficult
                case Bonus.BULLET:
                    Global.hero.bullets += 15
            Global.bonuses.discard(self)
            return

    def drawFigure(self):
        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        match self.type:
            case Bonus.HEALTH:
                pygame.draw.polygon(Global.screen, self.color, self.getCross())
            case Bonus.SCORE:
                pygame.draw.polygon(Global.screen, self.color, self.getArrow())
            case Bonus.BULLET:
                pygame.draw.polygon(Global.screen, self.color, self.getRhombus())

    def getArrow(self):
        return [[self.shape.x + 15, self.shape.y],
                [self.shape.x, self.shape.y + 15],
                [self.shape.x + 7, self.shape.y + 22],
                [self.shape.x + 15, self.shape.y + 13],
                [self.shape.x + 23, self.shape.y + 22],
                [self.shape.x + 30, self.shape.y + 15],
                [self.shape.x + 15, self.shape.y]]

    def getRhombus(self):
        return [[self.shape.x + 15, self.shape.y],
                [self.shape.x, self.shape.y + 15],
                [self.shape.x + 15, self.shape.y + 30],
                [self.shape.x + 30, self.shape.y + 15]]

    def getCross(self):
        return [[self.shape.x + 10, self.shape.y],
                [self.shape.x + 10, self.shape.y + 10],
                [self.shape.x, self.shape.y + 10],
                [self.shape.x, self.shape.y + 20],
                [self.shape.x + 10, self.shape.y + 20],
                [self.shape.x + 10, self.shape.y + 30],
                [self.shape.x + 20, self.shape.y + 30],
                [self.shape.x + 20, self.shape.y + 20],
                [self.shape.x + 30, self.shape.y + 20],
                [self.shape.x + 30, self.shape.y + 10],
                [self.shape.x + 20, self.shape.y + 10],
                [self.shape.x + 20, self.shape.y],
                [self.shape.x + 10, self.shape.y]]

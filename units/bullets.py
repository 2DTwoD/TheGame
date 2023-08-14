import pygame

from other.glb import Global
from other.unit_interfaces import UnitI
from other.unit_parameters import Color, Pair


class Bullet(UnitI):
    HERO = 0
    ENEMY = 1
    move = 10
    damage = 50

    def __init__(self, x, y, direction, target=ENEMY):
        UnitI.__init__(self, x, y, 5, 5)
        self.speed.x = self.move * direction
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))

        self.delFlag = False
        if target == Bullet.ENEMY:
            self.function = self.enemyTest
            self.color = Color(255, 255, 255)
        else:
            self.function = self.heroTest
            self.color = Color(237, 28, 36)

    def singleEngine(self):
        self.coordinates.x += self.speed.x
        if self.coordinates.x > Global.SCREEN_SIZE[0] or self.coordinates.x < 0:
            Global.bullets.discard(self)
        for wall in Global.walls:
            if self.hitTest(wall):
                Global.bullets.discard(self)
                return
        self.function()

    def enemyTest(self):
        for enemy in Global.enemies:
            if self.hitTest(enemy):
                Global.bullets.discard(self)
                enemy.setDamage(Bullet.damage, self.move)
                return

    def heroTest(self):
        if self.hitTest(Global.hero):
            Global.bullets.discard(self)
            Global.hero.setDamage(self)
            return

    def drawFigure(self):
        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)

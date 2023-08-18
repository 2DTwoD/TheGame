import pygame

from other.glb import Global
from other.unit_interfaces import UnitI
from other.unit_parameters import Colors


class Bullet(UnitI):
    HERO = 0
    ENEMY = 1
    move = 10

    def __init__(self, x, y, direction, damage, target=ENEMY):
        UnitI.__init__(self, x - 2, y - 2, 5, 5)
        self.speed.x = Bullet.move * direction
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.damage = damage
        self.delFlag = False
        if target == Bullet.ENEMY:
            self.function = self.enemyTest
            self.color = Colors.WHITE
        else:
            self.function = self.heroTest
            self.color = Colors.RED

    def singleEngine(self):
        if self.coordinates.x > Global.SCREEN_SIZE[0] or self.coordinates.x < 0:
            Global.bullets.discard(self)
        for wall in Global.walls:
            if self.hitTest(wall):
                Global.bullets.discard(self)
                return
        self.function()
        self.coordinates.x += self.speed.x

    def enemyTest(self):
        for enemy in Global.enemies:
            if self.hitTest(enemy):
                Global.bullets.discard(self)
                enemy.setDamage(Global.hero.damage, Bullet.move)
                return

    def heroTest(self):
        if self.hitTest(Global.hero):
            Global.bullets.discard(self)
            Global.hero.setDamage(self.damage)
            return

    def drawFigure(self):
        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        pygame.draw.rect(Global.screen, self.color, self.shape, 0)

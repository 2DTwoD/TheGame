import pygame

from other.glb import Global
from other.unit_interfaces import UnitI
from other.unit_parameters import Color


class Bullet(UnitI):
    move = 15
    damage = 3

    def __init__(self, x, y, direction):
        UnitI.__init__(self, x, y, 5, 5)
        self.move = -self.move if direction != 1 else self.move
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.color = Color(255, 255, 255)
        self.delFlag = False

    def singleEngine(self):
        self.coordinates.x += self.move

        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        if self.coordinates.x > Global.SCREEN_SIZE[0] or self.coordinates.x < 0:
            Global.bullets.discard(self)
        for wall in Global.walls:
            if self.hitTest(wall):
                Global.bullets.discard(self)
                return
        for enemy in Global.enemies:
            if self.hitTest(enemy):
                Global.bullets.discard(self)
                enemy.setDamage(Bullet.damage)
                return
        pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)

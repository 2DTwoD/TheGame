from random import random, randint

import pygame

from other.glb import Global
from other.unit_interfaces import GravityUnitI, Attributes
from other.unit_parameters import Color
from units.bonus import Bonus
from units.bullets import Bullet


class Enemy(GravityUnitI):
    acceleration = 0.2
    damageTime = 10

    def __init__(self, x, y, width, height, color: Color):
        GravityUnitI.__init__(self, x, y, width, height)
        self.color = color
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.health = 30 + 100 * Global.difficult / Global.maxDifficult
        self.jumpCount = 0
        self.shootCount = 0
        self.direction = 1 if self.coordinates.x < Global.hero.coordinates.x else -1
        self.damageAnimation = 0
        self.damage = 5 + int(20 * Global.difficult / Global.maxDifficult)
        self.maxSpeed = 1 + random() * (1 + Global.difficult) / Global.maxDifficult
        self.behavior = randint(0, 2)
        self.canJump = randint(0, 1)
        self.canShoot = randint(0, 1)
        self.shootPeriod = 60 + 15 * randint(Global.maxDifficult - Global.difficult, Global.maxDifficult)
        self.jumpPeriod = 60 + 15 * randint(Global.maxDifficult - Global.difficult, Global.maxDifficult)

    def accAction(self):
        self.speed.x += Enemy.acceleration * self.direction
        if self.speed.x > self.maxSpeed:
            self.speed.x = self.maxSpeed
        elif self.speed.x < -self.maxSpeed:
            self.speed.x = -self.maxSpeed

    def singleEngine(self):
        match self.behavior:
            case 0:
                self.speed.x = 0
            case 1:
                if self.speed.x == 0:
                    self.direction *= -1
                self.accAction()
            case 2:
                if self.coordinates.x < Global.hero.coordinates.x - Global.hero.dimensions.x / 2:
                    self.direction = 1
                    self.accAction()
                elif self.coordinates.x > Global.hero.coordinates.x + Global.hero.dimensions.x / 2:
                    self.direction = -1
                    self.accAction()
                else:
                    if self.speed.x * self.direction > 0:
                        self.speed.x -= Enemy.acceleration * self.direction
                    else:
                        self.speed.x = 0
        if self.speed.y > self.maxSpeed * 8:
            self.speed.y = self.maxSpeed * 8

        if self.canShoot:
            if self.shootCount < self.shootPeriod:
                self.shootCount += 1
            else:
                self.shootCount = 0
                Global.bullets.add(Bullet(self.middle_x,
                                          self.coordinates.y + self.dimensions.y / 2,
                                          self.direction, self.damage, Bullet.HERO))
        if self.canJump:
            if self.jumpCount < self.jumpPeriod:
                self.jumpCount += 1
            else:
                self.jumpCount = 0
                if self.onGround:
                    self.speed.y = -self.maxSpeed * 8

        if self.damageAnimation > 0:
            self.damageAnimation -= 1
        for enemy in Global.enemies:
            if enemy == self:
                continue
            self.getHitEngine(enemy)

    def drawFigure(self):
        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        if self.damageAnimation % 2 == 0:
            pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)

    def setDamage(self, value: int, bDirection: int):
        self.health -= value
        self.speed.x += bDirection
        self.damageAnimation = Enemy.damageTime
        if self.health < 0:
            Global.enemies.discard(self)
            Global.levelCreator.score += 50 * Global.difficult
            if random() > Global.difficult / Global.maxDifficult:
                Global.bonuses.add(Bonus(self.coordinates.x, self.coordinates.y))

    def falling(self):
        Global.enemies.discard(self)

    def downHit(self, obj: Attributes):
        GravityUnitI.downHit(self, obj)
        if isinstance(obj, Enemy):
            obj.onGround = False

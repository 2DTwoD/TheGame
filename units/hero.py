import pygame

from other.glb import Global
from other.unit_interfaces import GravityUnitI, Attributes
from other.unit_parameters import Color, Pair
from units.bullets import Bullet
from units.enemy import Enemy


class Hero(GravityUnitI):
    maxSpeed = 6
    acceleration = 0.5
    reloadCicle = 5
    damageTime = 60

    def __init__(self):
        GravityUnitI.__init__(self, 0, 0, 25, 25)
        self.color = Color(255, 255, 255)
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.direction = 1
        self.currentReload = Hero.reloadCicle
        self.damageAnimation = 0
        self._health = 100
        self.verticalStep = True

    def singleEngine(self):
        if Global.keys[pygame.K_d]:
            self.direction = 1
        if Global.keys[pygame.K_a]:
            self.direction = -1
        if not (Global.keys[pygame.K_d] + Global.keys[pygame.K_a]):
            if self.speed.x * self.direction > 0:
                self.speed.x -= Hero.acceleration * self.direction
            else:
                self.speed.x = 0
        else:
            self.speed.x += Hero.acceleration * self.direction
            if self.speed.x > Hero.maxSpeed:
                self.speed.x = Hero.maxSpeed
            elif self.speed.x < -Hero.maxSpeed:
                self.speed.x = -Hero.maxSpeed

        if self.currentReload > 0:
            self.currentReload -= 1

        if self.speed.y > Hero.maxSpeed * 3:
            self.speed.y = Hero.maxSpeed * 3

        if Global.keys[pygame.K_SPACE] and self.currentReload == 0 and Global.titles.bullets > 0:
            self.currentReload = Hero.reloadCicle
            Global.bullets.add(Bullet(self.middle_x,
                                      self.coordinates.y + self.dimensions.y / 2,
                                      self.direction))
            Global.titles.bullets -= 1

        if Global.keys[pygame.K_w] and self.verticalStep:
            if self.onGround:
                self.speed.y = -Hero.maxSpeed * 1.2
            self.speed.y -= 1.3
            if self.speed.y < -Hero.maxSpeed * 3:
                self.speed.y = -Hero.maxSpeed * 3
                self.verticalStep = False
        else:
            self.verticalStep = self.onGround

        if self.damageAnimation <= 0:
            for enemy in Global.enemies:
                if self.hitTest(enemy):
                    self.setDamage(enemy)
        else:
            self.damageAnimation -= 1

    def upHit(self, obj: Attributes):
        GravityUnitI.upHit(self, obj)
        self.verticalStep = self.onGround

    def drawFigure(self):
        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        if self.damageAnimation % 2 == 0:
            pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)

    def setDamage(self, damageSource):
        if self.damageAnimation != 0:
            return
        self.damageAnimation = Hero.damageTime
        if isinstance(damageSource, Enemy):
            pair = Pair(self.speed.x, self.speed.y)
            self.speed.x = damageSource.speed.x
            self.speed.y = damageSource.speed.y
            damageSource.speed.x = pair.x
            damageSource.speed.y = pair.y
            self.health -= damageSource.damage
        elif isinstance(damageSource, int):
            self.health -= damageSource

    def falling(self):
        self.coordinates.y = 0
        self.setDamage(50)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > 100:
            Global.titles.scores += 10
            return
        elif value < 0:
            print("Game Over!")
        self._health = value

import pygame

from other.glb import Global
from other.unit_interfaces import GravityUnitI, Attributes
from other.unit_parameters import Pair, Colors
from units.bullets import Bullet
from units.enemy import Enemy


class Hero(GravityUnitI):
    maxSpeed = 6
    acceleration = 0.5
    reloadCicle = 5
    damageTime = 60
    damage = 50

    def __init__(self):
        GravityUnitI.__init__(self, 0, 0, 25, 25)
        self.color = Colors.WHITE
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.direction = 1
        self.currentReload = Hero.reloadCicle
        self.damageAnimation = 0
        self._health = 100
        self._bullets = 100
        self.verticalStep = True
        self.firstPushFlag = False

    def reInit(self):
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.direction = 1
        self.currentReload = Hero.reloadCicle
        self.damageAnimation = 0
        self.health = 100
        self.bullets = 100
        self.verticalStep = True
        self.coordinates.x = 0
        self.coordinates.y = 0

    def singleEngine(self):
        if Global.keys[pygame.K_RIGHT]:
            self.direction = 1
        if Global.keys[pygame.K_LEFT]:
            self.direction = -1
        if not (Global.keys[pygame.K_RIGHT] + Global.keys[pygame.K_LEFT]):
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

        if (Global.keys[pygame.K_LSHIFT] + Global.keys[pygame.K_LALT] + Global.keys[pygame.K_s]) and self.currentReload == 0 and self.bullets > 0:
            self.currentReload = Hero.reloadCicle
            Global.bullets.add(Bullet(self.middle_x,
                                      self.coordinates.y + self.dimensions.y / 2,
                                      self.direction, Hero.damage))
            self.bullets -= 1

        if Global.keys[pygame.K_UP] and self.verticalStep:
            if not self.firstPushFlag:
                self.speed.y = -Hero.maxSpeed * 1.2
                self.firstPushFlag = True
            self.speed.y -= 1.3
            if self.speed.y < -Hero.maxSpeed * 3:
                self.speed.y = -Hero.maxSpeed * 3
                self.verticalStep = False
        else:
            self.verticalStep = self.onGround
            self.firstPushFlag = False

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
            pygame.draw.rect(Global.screen, self.color, self.shape, 0)

    def setDamage(self, damageSource):
        if self.damageAnimation != 0:
            return
        self.damageAnimation = Hero.damageTime
        self.verticalStep = False
        if isinstance(damageSource, Enemy):
            pair = Pair(self.speed.x, self.speed.y)
            self.speed.x = damageSource.speed.x
            self.speed.y = damageSource.speed.y
            damageSource.speed.x = pair.x
            damageSource.speed.y = pair.y
            self.health -= damageSource.damage
        elif isinstance(damageSource, int):
            self.health -= damageSource
        elif isinstance(damageSource, Bullet):
            self.health -= damageSource.damage

    def falling(self):
        self.coordinates.y = 0
        self.damageAnimation = 0
        self.setDamage(50)

    def raising(self):
        self.coordinates.y = 0
        self.speed.y = 0
        self.upHit(Attributes(Pair(0, 0), Pair(0, 0)))

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > 100:
            Global.levelCreator.score += 20 * Global.difficult
            self._health = 100
            return
        elif value <= 0:
            Global.resetGame()
            return
        self._health = value

    @property
    def bullets(self):
        return self._bullets

    @bullets.setter
    def bullets(self, value):
        if value <= 500:
            self._bullets = value
        else:
            Global.levelCreator.score += 20 * Global.difficult
            self._bullets = 500

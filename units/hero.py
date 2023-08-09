import pygame

from other.glb import Global
from other.unit_interfaces import GravityUnitI
from other.unit_parameters import Color, KeyMatrix
from units.bullet import Bullet


class Hero(GravityUnitI):
    move = 5
    reloadCicle = 5

    def __init__(self):
        GravityUnitI.__init__(self, 0, 0, 25, 25)
        self.color = Color(255, 255, 255)
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.keyMatrix = KeyMatrix()
        self.direction = 1
        self.currentReload = Hero.reloadCicle

    def singleEngine(self):
        if self.coordinates.x < 0:
            self.coordinates.x = 0

        if self.coordinates.x > Global.SCREEN_SIZE[0] - self.dimensions.x:
            self.coordinates.x = Global.SCREEN_SIZE[0] - self.dimensions.x

        if self.coordinates.y < 0:
            self.coordinates.y = 0
            self.speed.y = 0

        if self.coordinates.y > Global.SCREEN_SIZE[1]:
            self.coordinates.y = -self.dimensions.y

        if Global.keys[pygame.K_d]:
            self.direction = 1
            self.speed.x = Hero.move
        if Global.keys[pygame.K_a]:
            self.direction = 0
            self.speed.x = -Hero.move
        if not (Global.keys[pygame.K_d] + Global.keys[pygame.K_a]):
            self.speed.x = 0

        if self.currentReload > 0:
            self.currentReload -= 1

        if Global.keys[pygame.K_SPACE] and self.currentReload == 0:
            self.currentReload = Hero.reloadCicle
            Global.bullets.add(Bullet(self.middle_x,
                                      self.coordinates.y + self.dimensions.y / 2,
                                      self.direction))
        if Global.keys[pygame.K_w] and self.onGround:
            self.speed.y = -Hero.move * 3

        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        pygame.draw.rect(Global.screen, self.color.get(), self.shape, 0)
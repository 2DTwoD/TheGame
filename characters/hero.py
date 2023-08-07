
import pygame

from other.glb import Global
from other.unit_interfaces import Unit
from other.unit_parameters import Pair, Color, KeyMatrix


class Hero(Unit):
    def __init__(self, glb: Global, gravity: int):
        Unit.__init__(self, 0, 0, 25, 25)
        self.glb = glb
        self.speed = Pair(0, 0)
        self.color = Color(255, 255, 255)
        self.shape = pygame.Rect(*(self.coordinates.get() + self.dimensions.get()))
        self.keyMatrix = KeyMatrix()
        self.onGround = False
        if gravity != 0:
            gravity = 1

    def updateShape(self):
        if self.keyMatrix.right:
            self.speed.x = 5
        if self.keyMatrix.left:
            self.speed.x = -5
        if not self.keyMatrix.right and not self.keyMatrix.left:
            self.speed.x = 0

        self.coordinates.y += self.speed.y
        self.coordinates.x += self.speed.x
        if self.speed.x > 0:
            self.hitTest(Unit.RIGHT)
        elif self.speed.x < 0:
            self.hitTest(Unit.LEFT)
        if self.speed.y > 0:
            self.hitTest(Unit.DOWN)
        elif self.speed.y < 0:
            self.hitTest(Unit.UP)

        if self.coordinates.y > self.glb.screen.get_size()[1]:
            self.coordinates.y = -self.dimensions.y

        if self.coordinates.x < 0:
            self.coordinates.x = 0

        if self.coordinates.x > self.glb.screen.get_size()[0] - self.dimensions.x:
            self.coordinates.x = self.glb.screen.get_size()[0] - self.dimensions.x

        self.shape.x = self.coordinates.x
        self.shape.y = self.coordinates.y
        pygame.draw.rect(self.glb.screen, self.color.get(), self.shape, 0)

    def hitTest(self, direction):
        self.onGround = False
        for wall in self.glb.walls:
            if direction == Unit.UP or direction == Unit.DOWN:
                if self.shape.x + self.dimensions.x <= wall.coordinates.x \
                        or self.shape.x >= wall.coordinates.x + wall.dimensions.x:
                    continue
                if wall.shape.y - self.dimensions.y < self.coordinates.y < wall.shape.y + wall.dimensions.y:
                    self.coordinates.y -= self.speed.y
                    self.speed.y = 0
                    self.onGround = direction == Unit.DOWN
            elif direction == Unit.LEFT or direction == Unit.RIGHT:
                if self.shape.y + self.dimensions.y <= wall.coordinates.y \
                        or self.shape.y >= wall.coordinates.y + wall.dimensions.y:
                    continue
                if wall.shape.x + wall.dimensions.x > self.coordinates.x > wall.shape.x - self.dimensions.x:
                    self.coordinates.x -= self.speed.x
                    self.speed.x = 0

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.keyMatrix.left = True
            if event.key == pygame.K_RIGHT:
                self.keyMatrix.right = True
            if event.key == pygame.K_UP and self.onGround:
                self.speed.y = -15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.keyMatrix.left = False
            if event.key == pygame.K_RIGHT:
                self.keyMatrix.right = False

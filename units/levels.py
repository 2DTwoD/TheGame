from random import randrange, randint, random

from other.glb import Global
from other.unit_parameters import Color, Colors
from units.bonus import Bonus
from units.enemy import Enemy
from units.wall import Wall


class WallCreator:

    wallPeriod = 180
    wallThickness = 50
    minGap = 100
    maxEnemies = 3
    maxBonuses = 2

    def __init__(self):
        self.curTime = 0
        self.startWallX = 0
        curY = 0
        while curY < Global.screenHeight():
            self.getRelief(curY)
            curY += WallCreator.wallPeriod

    def run(self):
        if self.curTime < WallCreator.wallPeriod / Global.worldSpeed:
            self.curTime += 1
        else:
            self.curTime = 0
            Global.titles.scores += 5
            self.getRelief(-WallCreator.wallThickness)

    def getRelief(self, y):
        self.startWallX = 0
        walls = []
        while self.startWallX < Global.screenWidth():
            if random() >= (0.1 * (1 + Global.difficult)):
                walls.append(Wall(self.startWallX, y, WallCreator.minGap, WallCreator.wallThickness, Colors.BROWN))
            self.startWallX += WallCreator.minGap

        if len(walls) == Global.screenWidth() / WallCreator.minGap:
            del walls[randint(0, Global.screenWidth() / WallCreator.minGap) - 1]

        Global.walls.update(walls)

        numOfEnemy = randint(0, WallCreator.maxEnemies)
        while numOfEnemy < WallCreator.maxEnemies:
            Global.enemies.add(Enemy(randrange(Global.screenWidth()), y, 25, 25, Color(237, 28, 36)))
            numOfEnemy += 1

        numOfBonuses = randint(0, WallCreator.maxBonuses)
        while numOfBonuses < WallCreator.maxBonuses:
            Global.bonuses.add(Bonus(randrange(Global.screenWidth()), y - 30 - randint(0, 100)))
            numOfBonuses += 1

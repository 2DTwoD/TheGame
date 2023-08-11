from random import randrange, randint, random

from other.glb import Global
from other.unit_parameters import Color
from units.enemy import Enemy
from units.wall import Wall


class WallCreator:

    wallPeriod = 180
    minGap = 100
    maxEnemies = 10

    def __init__(self):
        self.curTime = 0
        self.startWallX = 0
        self.floorPossibility = 7

    def run(self):
        if self.curTime < WallCreator.wallPeriod / Global.worldSpeed:
            self.curTime += 1
        else:
            self.curTime = 0
            self.startWallX = 0
            hole = 0
            walls = []
            while self.startWallX < Global.screenWidth():
                if random() >= (0.1 * self.floorPossibility):
                    walls.append(Wall(self.startWallX, -50, WallCreator.minGap, 50, Color(128, 128, 0)))
                else:
                    hole = 1
                self.startWallX += WallCreator.minGap

            if hole == 0:
                del walls[randint(0, Global.screenWidth() / WallCreator.minGap) - 1]

            Global.walls.update(walls)

            numOfEnemy = randint(0, 3)
            while numOfEnemy < WallCreator.maxEnemies:
                Global.enemies.add(Enemy(randrange(Global.screenWidth()), 0, 25, 25, Color(237, 28, 36)))
                numOfEnemy += 1

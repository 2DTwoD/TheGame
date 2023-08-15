from random import randrange, randint, random

from other.glb import Global
from other.unit_parameters import Colors
from units.bonus import Bonus
from units.enemy import Enemy
from units.wall import Wall


class LevelCreator:

    wallPeriod = 180
    difficultPeriod = 600
    wallThickness = 50
    minGap = 100
    maxEnemies = 5
    maxBonuses = 3

    def __init__(self):
        self.curWallTime = 0
        self.curDifficultTime = 0
        self.startWallX = 0
        self.scores = 0
        self.reInit()

    def run(self):

        if self.curWallTime < LevelCreator.wallPeriod / Global.worldSpeed:
            self.curWallTime += 1
        else:
            self.curWallTime = 0
            self.scores += 5 * Global.difficult
            self.getRelief(-LevelCreator.wallThickness)

        if self.curDifficultTime < LevelCreator.difficultPeriod:
            self.curDifficultTime += 1
        else:
            if Global.difficult < Global.maxDifficult:
                Global.difficult += 1
            self.curDifficultTime = 0
            Global.worldSpeed = int(1 + 3 * Global.difficult / Global.maxDifficult)

    def reInit(self):
        self.curWallTime = 0
        self.curDifficultTime = 0
        self.startWallX = 0
        self.scores = 0
        curY = -LevelCreator.wallThickness
        while curY < Global.screenHeight():
            self.getRelief(curY)
            curY += LevelCreator.wallPeriod

    def getRelief(self, y):
        self.startWallX = 0
        walls = []
        difKoef = Global.difficult / Global.maxDifficult
        difKoefRev = 1 - difKoef
        while self.startWallX < Global.screenWidth():
            if random() >= difKoef - 0.2 * difKoef:
                walls.append(Wall(self.startWallX, y, LevelCreator.minGap, LevelCreator.wallThickness, Colors.BROWN))
            self.startWallX += LevelCreator.minGap

        if len(walls) == Global.screenWidth() / LevelCreator.minGap:
            del walls[randint(0, Global.screenWidth() / LevelCreator.minGap) - 1]
        elif len(walls) == 0:
            walls.append(Wall(randint(0, Global.screenWidth() - LevelCreator.minGap), y, LevelCreator.minGap, LevelCreator.wallThickness, Colors.BROWN))

        Global.walls.update(walls)

        numOfEnemy = randint(int(difKoefRev * LevelCreator.maxEnemies), LevelCreator.maxEnemies)
        while numOfEnemy < LevelCreator.maxEnemies:
            Global.enemies.add(Enemy(randrange(Global.screenWidth()), y, 25, 25, Colors.RED))
            numOfEnemy += 1

        numOfBonuses = randint(int(difKoefRev * LevelCreator.maxBonuses), LevelCreator.maxBonuses)
        while numOfBonuses < LevelCreator.maxBonuses:
            Global.bonuses.add(Bonus(randrange(Global.screenWidth()), y - 30 - randint(0, 100)))
            numOfBonuses += 1

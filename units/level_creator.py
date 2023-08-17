from random import randrange, randint, random

from other.glb import Global
from other.unit_parameters import Colors
from units.bonus import Bonus
from units.enemy import Enemy
from units.wall import Wall


class LevelCreator:
    difficultPeriod = 60 * Global.FPS
    wallThickness = 50
    minGap = 100
    wallDistance = 200
    maxEnemies = 7
    maxBonuses = 4

    def __init__(self):
        self.curWallDistance = 0
        self.curDifficultTime = 0
        self.startWallX = 0
        self._score = 0
        self.reInit()

    def run(self):
        if Global.difficult < Global.maxDifficult:
            if self.curDifficultTime < LevelCreator.difficultPeriod:
                self.curDifficultTime += 1
            else:
                Global.difficult += 1
                self.curDifficultTime = 0
                Global.worldSpeed = int(1 + 2 * pow(Global.difficult / Global.maxDifficult, 1.5))

        if self.curWallDistance < LevelCreator.wallDistance:
            self.curWallDistance += Global.worldSpeed
        else:
            self.curWallDistance = 0
            self.score += 5 * Global.difficult
            self.getRelief(-LevelCreator.wallThickness)

    def reInit(self):
        self.curWallDistance = 0
        self.curDifficultTime = 0
        self.startWallX = 0
        self.score = 0
        curY = -LevelCreator.wallThickness
        while curY < Global.screenHeight():
            self.getRelief(curY)
            curY += LevelCreator.wallDistance

    def getRelief(self, y):
        self.startWallX = 0
        walls = []
        difKoef = Global.difficult / Global.maxDifficult
        difKoefRev = 1 - difKoef
        wallColor = Global.wallColors[Global.difficult - 1] if Global.difficult <= len(
            Global.wallColors) else Global.backgroundColors[-1]
        while self.startWallX < Global.screenWidth():
            if random() >= difKoef - 0.2 * difKoef:
                walls.append(Wall(self.startWallX, y, LevelCreator.minGap, LevelCreator.wallThickness, wallColor))
            self.startWallX += LevelCreator.minGap

        if len(walls) == Global.screenWidth() / LevelCreator.minGap:
            del walls[randint(0, Global.screenWidth() / LevelCreator.minGap) - 1]
        elif len(walls) == 0:
            walls.append(Wall(randint(0, Global.screenWidth() - LevelCreator.minGap), y, LevelCreator.minGap,
                              LevelCreator.wallThickness, wallColor))

        Global.walls.update(walls)

        numOfEnemy = randint(int(difKoefRev * LevelCreator.maxEnemies), LevelCreator.maxEnemies)
        while numOfEnemy < LevelCreator.maxEnemies:
            Global.enemies.add(Enemy(randrange(Global.screenWidth()), y - LevelCreator.wallThickness, 25, 25, Colors.RED))
            numOfEnemy += 1

        numOfBonuses = randint(int(difKoefRev * LevelCreator.maxBonuses), LevelCreator.maxBonuses)
        while numOfBonuses < LevelCreator.maxBonuses:
            Global.bonuses.add(Bonus(randrange(Global.screenWidth() - 30), y - 30 - randint(0, LevelCreator.wallDistance - LevelCreator.wallThickness - 30)))
            numOfBonuses += 1

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

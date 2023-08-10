from other.glb import Global
from other.unit_parameters import Color
from units.wall import Wall


class WallCreator:

    wallPeriod = 60

    def __init__(self):
        self.curTime = 0

    def run(self):
        if self.curTime < WallCreator.wallPeriod:
            self.curTime += 1
        else:
            self.curTime = 0
            Global.walls.add(Wall(0, -50, Global.SCREEN_SIZE[0], 50, Color(128, 128, 0)))


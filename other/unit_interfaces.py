from other.glb import Global
from other.unit_parameters import Pair


class Attributes:

    def __init__(self, coordinates: Pair, dimensions: Pair):
        self.coordinates = coordinates
        self.dimensions = dimensions

    @property
    def left_x(self):
        return self.coordinates.x

    @property
    def right_x(self):
        return self.coordinates.x + self.dimensions.x

    @property
    def up_y(self):
        return self.coordinates.y

    @property
    def down_y(self):
        return self.coordinates.y + self.dimensions.y

    @property
    def middle_x(self):
        return self.coordinates.x + (self.right_x - self.left_x) / 2

    @property
    def middle_y(self):
        return self.coordinates.y + (self.down_y - self.up_y) / 2


class UnitI(Attributes):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, x, y, width, height):
        Attributes.__init__(self, Pair(x, y), Pair(width, height))
        self.speed = Pair(0, 0)
        self.shape = None

    def draw(self):
        self.singleEngine()
        self.commonEngine()

    def singleEngine(self):
        pass

    def commonEngine(self):
        self.coordinates.x += self.speed.x
        self.coordinates.y += self.speed.y
        self.coordinates.y += Global.worldSpeed

    def hitTest(self, obj: Attributes):
        return self.right_x + self.speed.x > obj.left_x and self.left_x + self.speed.x < obj.right_x and \
                self.down_y + self.speed.y > obj.up_y and self.up_y + self.speed.y < obj.down_y


class GravityUnitI(UnitI):
    def __init__(self, x, y, width, height):
        UnitI.__init__(self, x, y, width, height)
        self.onGround = False

    def commonEngine(self):
        self.speed.y += Global.g
        self.onGround = False
        for wall in Global.walls:
            if self.hitTest(wall):
                if self.down_y <= wall.up_y:
                    self.coordinates.y = wall.up_y - self.dimensions.y
                    self.speed.y = 0
                    self.onGround = True
                    continue
                elif self.up_y >= wall.down_y:
                    self.coordinates.y = wall.down_y
                    self.speed.y = 0
                    continue
                if self.right_x <= wall.left_x:
                    self.coordinates.x = wall.left_x - self.dimensions.x
                    self.speed.x = 0
                elif self.left_x >= wall.right_x:
                    self.coordinates.x = wall.right_x
                    self.speed.x = 0
        UnitI.commonEngine(self)

class WallI(Attributes):
    def __init__(self, x, y, width, height):
        Attributes.__init__(self, Pair(x, y), Pair(width, height))

    def draw(self):
        self.singleEngine()
        self.commonEngine()

    def singleEngine(self):
        pass

    def commonEngine(self):
        self.coordinates.y += Global.worldSpeed

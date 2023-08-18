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
        if Global.pause:
            return
        self.singleEngine()
        self.commonEngine()
        self.drawFigure()

    def singleEngine(self):
        pass

    def commonEngine(self):
        self.coordinates.x += self.speed.x
        self.coordinates.y += self.speed.y
        self.coordinates.y += Global.worldSpeed

    def hitTest(self, obj: Attributes):
        return self.right_x + self.speed.x > obj.left_x and self.left_x + self.speed.x < obj.right_x and \
               self.down_y + self.speed.y > obj.up_y and self.up_y + self.speed.y < obj.down_y

    def drawFigure(self):
        pass


class GravityUnitI(UnitI):
    def __init__(self, x, y, width, height):
        UnitI.__init__(self, x, y, width, height)
        self.onGround = False

    def draw(self):
        if Global.pause:
            return
        self.speed.y += Global.g
        UnitI.draw(self)
        UnitI.commonEngine(self)
        if self.coordinates.x < 0:
            self.coordinates.x = 0
            self.speed.x = 0
        if self.coordinates.x > Global.screenWidth() - self.dimensions.x:
            self.coordinates.x = Global.screenWidth() - self.dimensions.x
            self.speed.x = 0
        if self.coordinates.y < 0:
            self.raising()
        if self.coordinates.y > Global.screenHeight() + self.dimensions.y:
            self.falling()

    def commonEngine(self):
        if self.speed.y != 0:
            self.onGround = False
        for wall in Global.walls:
            self.getHitEngine(wall)

    def getHitEngine(self, obj: Attributes):
        if self.hitTest(obj):
            if self.down_y <= obj.up_y:
                self.downHit(obj)
                return
            elif self.up_y >= obj.down_y:
                self.upHit(obj)
                return
            if self.right_x <= obj.left_x:
                self.rightHit(obj)
            elif self.left_x >= obj.right_x:
                self.leftHit(obj)

    def falling(self):
        pass

    def raising(self):
        pass

    def downHit(self, obj: Attributes):
        self.coordinates.y = obj.up_y - self.dimensions.y
        self.speed.y = 0
        self.onGround = True

    def upHit(self, obj: Attributes):
        self.coordinates.y = obj.down_y
        self.speed.y = 0
        self.onGround = False

    def rightHit(self, obj: Attributes):
        self.coordinates.x = obj.left_x - self.dimensions.x
        self.speed.x = 0

    def leftHit(self, obj: Attributes):
        self.coordinates.x = obj.right_x
        self.speed.x = 0

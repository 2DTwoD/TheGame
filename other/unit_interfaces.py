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

class UnitI(Attributes):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, x, y, width, height):
        Attributes.__init__(self, Pair(x, y), Pair(width, height))
        self.onGround = True
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
        # if self.speed.x > 0:
        #     self.hitWallTest(UnitI.RIGHT)
        # elif self.speed.x < 0:
        #     self.hitWallTest(UnitI.LEFT)
        # if self.speed.y > 0:
        #     self.hitWallTest(UnitI.DOWN)
        # elif self.speed.y < 0:
        #     self.hitWallTest(UnitI.UP)
        for wall in Global.walls:
            if self.speed.x != 0 and self.hitTestX(wall):
                self.coordinates.x -= self.speed.x
                self.speed.x = 0
            if self.speed.y != 0 and self.hitTestY(wall):
                self.coordinates.y -= self.speed.y
                self.speed.y = 0

        self.coordinates.y += Global.worldSpeed

    # def hitWallTest(self, direction):
    #     self.onGround = False
    #     for wall in Global.walls:
    #         if direction == UnitI.UP or direction == UnitI.DOWN:
    #             if self.shape.x + self.dimensions.x <= wall.coordinates.x \
    #                     or self.shape.x >= wall.coordinates.x + wall.dimensions.x:
    #                 continue
    #             if wall.coordinates.y - self.dimensions.y < self.coordinates.y < wall.coordinates.y + wall.dimensions.y:
    #                 self.coordinates.y -= self.speed.y
    #                 self.speed.y = 0
    #                 self.onGround = direction == UnitI.DOWN
    #         elif direction == UnitI.LEFT or direction == UnitI.RIGHT:
    #             if self.shape.y + self.dimensions.y <= wall.coordinates.y \
    #                     or self.shape.y >= wall.coordinates.y + wall.dimensions.y:
    #                 continue
    #             if wall.coordinates.x + wall.dimensions.x > self.coordinates.x > wall.coordinates.x - self.dimensions.x:
    #                 self.coordinates.x -= self.speed.x
    #                 self.speed.x = 0

    def hitTestX(self, obj: Attributes):
        if self.down_y > obj.up_y and self.up_y < obj.down_y:
            if self.right_x > obj.left_x and self.left_x < obj.right_x:
                return True
        return False

    def hitTestY(self, obj: Attributes):
        if self.right_x > obj.left_x and self.left_x < obj.right_x:
            if self.down_y >= obj.up_y and self.up_y <= obj.down_y:
                return True
        return False


class GravityUnitI(UnitI):
    def __init__(self, x, y, width, height):
        UnitI.__init__(self, x, y, width, height)

    def draw(self):
        self.singleEngine()
        self.commonEngine()
        self.speed.y += Global.g


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
